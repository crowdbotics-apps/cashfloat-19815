from django.conf import settings
from django.db import models


class ANCV(models.Model):
    "Generated Model"
    value = models.FloatField()
    qty = models.BigIntegerField()


class Caisse(models.Model):
    "Generated Model"
    cb = models.ManyToManyField("home.Cb", related_name="caisse_cb",)
    espece = models.OneToOneField(
        "home.Espece",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="caisse_espece",
    )
    date = models.DateTimeField(auto_now=True, null=True, blank=True,)
    signature = models.CharField(max_length=256, null=True, blank=True,)


# Create your models here.
