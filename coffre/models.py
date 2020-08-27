from django.conf import settings
from django.db import models


class Coffre(models.Model):
    "Generated Model"
    date = models.DateTimeField(auto_now=True,)
    signature = models.BigIntegerField()
    caisse = models.ManyToManyField(
        "caisse.Caisse", blank=True, related_name="coffre_caisse",
    )


# Create your models here.
