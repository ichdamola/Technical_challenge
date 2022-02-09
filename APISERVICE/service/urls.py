"""
service/urls.py
"""

from django.urls import path
from service import views

urlpatterns = [
    path("apiversion/", views.api_service_version),
]
