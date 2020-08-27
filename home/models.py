from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Espece(models.Model):
    "Generated Model"
    cent = models.BigIntegerField()
    cent2 = models.BigIntegerField()
    cent5 = models.BigIntegerField()
    cent10 = models.BigIntegerField()
    cent50 = models.BigIntegerField()
    euro1 = models.BigIntegerField()
    euro2 = models.BigIntegerField()
    euro5 = models.BigIntegerField()
    euro10 = models.BigIntegerField()
    euro20 = models.BigIntegerField()
    euro50 = models.BigIntegerField()
    euro100 = models.BigIntegerField()
    euro200 = models.BigIntegerField()
    euro500 = models.BigIntegerField()
    real = models.BigIntegerField()
    theorique = models.BigIntegerField()


class Cheque(models.Model):
    "Generated Model"
    real = models.BigIntegerField()
    theorique = models.BigIntegerField()
    nb = models.BigIntegerField()


class Cb(models.Model):
    "Generated Model"
    real = models.BigIntegerField()
    theorique = models.BigIntegerField()
    nbTickets = models.BigIntegerField()
    idTelecollect = models.BigIntegerField()
