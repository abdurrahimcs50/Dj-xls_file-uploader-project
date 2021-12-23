from django.db import models

# Create your models here.

class Company(models.Model):
    data = models.CharField(max_length=200, blank=True, null=True)
    valuta = models.CharField(max_length=200, blank=True, null=True)
    descrizione = models.CharField(max_length=200, blank=True, null=True)
    addebiti = models.CharField(max_length=200, blank=True, null=True)
    accrediti = models.CharField(max_length=200, blank=True, null=True)
    descrizioneestesa = models.CharField(max_length=1000, blank=True, null=True)
    