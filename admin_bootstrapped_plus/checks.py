""" System checks """
__author__ = 'George Karakostas'
__copyright__ = 'Copyright 2015, George Karakostas'
__licence__ = 'BSD-3'

from django.core.checks import register, Tags, Warning
from django.conf import settings


# noinspection PyUnusedLocal
@register(Tags.compatibility)
def check_settings(app_configs, **kwargs):
    """ Check that settings are implemented properly
    :param app_configs: a list of apps to be checks or None for all
    :param kwargs: keyword arguments
    :return: a list of errors
    """
    checks = []
    apps = settings.INSTALLED_APPS
    dca = 'django.contrib.admin'
    dab = 'django_admin_bootstrapped'
    dabp = 'admin_bootstrapped_plus'
    msg = ("`%s` and `%s` are required to be included in the `INSTALLED_APPS` setting, "
           "in this order and after `%s` so that the latter works.") % (dab, dca, dabp)
    if not {dab, dca}.issubset(apps):
        checks.append(Warning(msg, id='%s.W001' % dabp))
    elif not (apps.index(dabp) < apps.index(dab) < apps.index(dca)):
        checks.append(Warning(msg, id='%s.W002' % dabp))
    return checks
