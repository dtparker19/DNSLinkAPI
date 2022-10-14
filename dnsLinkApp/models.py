""" Models for the DNSLinkApp"""

from django.db import models

# Create your models here.
class DLink(models.Model):
    """_summary_

    Args:
        models (DLink): model for the dnslink entries
    """
    name = models.CharField(max_length=250)
    domain = models.URLField()
    location = models.CharField(max_length=250)
    username = models.CharField(max_length=250)