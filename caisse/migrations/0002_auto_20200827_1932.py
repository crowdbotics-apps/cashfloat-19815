# Generated by Django 2.2.15 on 2020-08-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caisse',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='caisse',
            name='signature',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]