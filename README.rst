==============================
Django Admin Bootstrapped Plus
==============================

*Django Admin Bootstrapped Plus* is a small Django app
which provides a *vertical sidebar* to the standard Django admin pages,
as provided by the required app
`Django Admin Bootstrapped <https://github.com/django-admin-bootstrapped/django-admin-bootstrapped>`_.

The vertical sidebar provides a stack of links to all models, grouped by the installed apps.

Detailed documentation soon to be published.

Dependencies
------------

- Python (3.4+)
- Django (1.8+): Web framework
- django-admin-bootstrapped (2.5+): provide a nicer admin interface experience

Quick how-to
------------

This is a quick guide on how to use it.

1. Install django-admin-bootstrapped-plus

  - Download source and place in project root
  - *Soon available as python package*

2. Dependencies:

  - Add the following to the ``requirements.txt`` file::

        Django==1.8.7
        django-admin-bootstrapped==2.5.6

  - Then run::

        $ sudo pip install -r requirements.txt

3. Settings

  - You need to install the app in ``INSTALLED_APPS`` before admin_bootstrapped and before admin,
    so that Django loads the templates properly::

        INSTALLED_APPS = (
            'admin_bootstrapped_plus',
            'django_admin_bootstrapped',
            'django.contrib.admin',
            # ...
        )

4. Start the development server and visit http://127.0.0.1:8000/admin/

That's it.

Footnote
--------

Any contribution to the project is highly appreciated and the best will be done to respond to it.
