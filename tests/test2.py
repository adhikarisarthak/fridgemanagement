from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
import users.views as user_views


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, user_views.register)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, user_views.profile)

