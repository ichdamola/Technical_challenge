from ipaddress import ip_address
from pyexpat import model
from django.db import models


class Service(models.Model):
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)
