"""
Tests declaration for Django Admin Bootstrapped Plus
"""
__author__ = 'George Karakostas'
__copyright__ = 'Copyright 2015, George Karakostas'
__licence__ = 'BSD-3'
__email__ = 'gkarak@9-dev.com'

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from admin_bootstrapped_plus.checks import check_settings


class Tests(TestCase):
    """ Tests for the app """
    @classmethod
    def setUpTestData(cls):
        """ Setup initial data:
        Create front page
        Create basic page
        Create user
        Create image
        :return: None
        """
        User.objects.create_superuser('admin', 'gkarak@9-dev.com', '1234')

    def setUp(self):
        """ Setup each test: login
        :return: None
        """
        self.client.login(username='admin', password='1234')

    def test_admin_page(self):
        """ Test that the context for the sidebar is correct
        and that the sidebar has got at least
        :return: None
        """
        response = self.client.get(reverse('admin:index'))
        self.assertIn('admin_app_list', response.context)
        self.assertContains(response, '<div class="panel-heading" role="tab" id="auth">')

    def test_checks(self):
        """ Test custom system checks
        :return: None
        """
        self.assertFalse(check_settings(None))

        apps = (
            'admin_bootstrapped_plus',
            'django_admin_bootstrapped',
            # 'admin_bootstrapped_plus',
            # 'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'mptt',
            'debug_toolbar',
            'guardian',
            'ninecms',
        )
        with self.settings(INSTALLED_APPS=apps):
            self.assertEqual(check_settings(None)[0].id, 'admin_bootstrapped_plus.W001')

        apps = (
            # 'admin_bootstrapped_plus',
            'django_admin_bootstrapped',
            'admin_bootstrapped_plus',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'mptt',
            'debug_toolbar',
            'guardian',
            'ninecms',
        )
        with self.settings(INSTALLED_APPS=apps):
            self.assertEqual(check_settings(None)[0].id, 'admin_bootstrapped_plus.W002')
