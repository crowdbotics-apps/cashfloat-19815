# Generated by Django 2.2.15 on 2020-08-27 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_cb_cheque_espece'),
    ]

    operations = [
        migrations.CreateModel(
            name='ANCV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('qty', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cb', models.ManyToManyField(related_name='caisse_cb', to='home.Cb')),
                ('espece', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caisse_espece', to='home.Espece')),
            ],
        ),
    ]