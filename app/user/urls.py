"""User urls."""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_view, name='register'),
]