"""
Test for user.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

class PublicUserTest(TestCase):
    """Tests for not authentication user."""
    ...
