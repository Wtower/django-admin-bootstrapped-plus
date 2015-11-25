""" Django Admin Bootstrap Plus custom template filters and tags """
__author__ = 'George Karakostas'
__copyright__ = 'Copyright 2015, George Karakostas'
__licence__ = 'BSD-3'
__email__ = 'gkarak@9-dev.com'

from django import template
from django.contrib import admin
from django.utils.text import capfirst
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils import six
from django.apps import apps

register = template.Library()


# noinspection PyProtectedMember
@register.assignment_tag(takes_context=True)
def get_app_list(context):
    """ Return a list of all applications
    Similar to the context `app_list` in index
    Code taken from contrib/admin/sites.py index()
    Similar concept in following old link, but in template context processor
    Disagreed with for overall performance reasons

    https://djangosnippets.org/snippets/1921/
    http://stackoverflow.com/questions/8893755/defining-a-custom-app-list-in-django-admin-index-page

    :param context
    :return: list of dictionaries
    """
    app_dict = {}
    request = context['request']
    site = admin.site
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = model_admin.has_module_permission(request)

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                }
                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=site.name)
                    except NoReverseMatch:  # pragma: nocover
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=site.name)
                    except NoReverseMatch:  # pragma: nocover
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'name': apps.get_app_config(app_label).verbose_name,
                        'app_label': app_label,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=site.name,
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # Sort the apps alphabetically.
    app_list = list(six.itervalues(app_dict))
    app_list.sort(key=lambda x: x['name'].lower())

    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])

    return app_list
