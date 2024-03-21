"""
Tests for admin customization
"""
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse



class AdminTests(TestCase):
    """Tests for admin."""
    def  setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='AdminName',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            username='TestName',
            password='testpass123',
        )


    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:auth_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)

    def test_edit_user_page(self):
        """Test user page works."""
        url = reverse('admin:auth_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works."""
        url = reverse('admin:auth_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

