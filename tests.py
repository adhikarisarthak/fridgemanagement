from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from fridge_app.models import Item, Fridge
from fridge_app.views import about, shopping, expired, fridges
import users.views as user_views


class TestUrls(SimpleTestCase):

    def test_about_url_resolves(self):
        url = reverse('fridge-about')
        self.assertEqual(resolve(url).func, about)

    def test_shopping_url_resolves(self):
        url = reverse('fridge-shopping')
        self.assertEqual(resolve(url).func, shopping)

    def test_expired_url_resolves(self):
        url = reverse('fridge-expired')
        self.assertEqual(resolve(url).func, expired)

    def test_fridges_url_resolves(self):
        url = reverse('fridge-detail')
        self.assertEqual(resolve(url).func, fridges)

    def test_fridge_create_url_resolves(self):
        url = reverse('fridge-create')
        self.assertEqual(resolve(url).func, fridge - create)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, user_views.register)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, user_views.profile)


class ItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.fridge = Fridge.objects.create(name='Test Fridge', user=self.user)
        self.item = Item.objects.create(
            name='Test Item',
            category='Test Category',
            qty=1,
            fridge=self.fridge,
            expiry_date=datetime.now().date() + timedelta(days=1)
        )

    def test_get_absolute_url(self):
        expected_url = reverse('item-detail', kwargs={'pk': self.item.pk})
        self.assertEqual(self.item.get_absolute_url(), expected_url)

    def test_is_expired(self):
        self.assertFalse(self.item.is_expired())
        expired_item = Item.objects.create(
            name='Expired Item',
            category='Expired Category',
            qty=1,
            fridge=self.fridge,
            expiry_date=datetime.now().date() - timedelta(days=1)
        )
        self.assertTrue(expired_item.is_expired())

    def test_fridge_name(self):
        self.assertEqual(self.item.fridge_name(), 'Test Fridge')
