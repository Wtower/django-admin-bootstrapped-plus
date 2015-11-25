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
        """ Test
        :return: None
        """
        response = self.client.get(reverse('admin:index'))
        self.assertIn('admin_app_list', response.context)
        self.assertContains(response, '<div class="panel-heading" role="tab" id="auth">')
