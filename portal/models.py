from django.db import models

# Create your models here.
class Warrior(models.Model):
    sibko = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    joined = models.DateField()
    clan = models.ForeignKey(Clan)

class Clan(models.Model):
    name = models.CharField()
