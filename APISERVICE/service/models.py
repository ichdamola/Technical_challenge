"""
service/models.py
"""

from django.db import models


class Service(models.Model):
    """
    Defines the Service database schema.

    Fields:
        ip_address (str): server/system ip address.
        mac_addres (str): server/system mac address.
    """

    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)
