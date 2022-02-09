"""
service/serializers.py
"""

from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("ip_address", "mac_address")
        model = Service
