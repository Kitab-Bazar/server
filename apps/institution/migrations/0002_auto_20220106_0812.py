# Generated by Django 3.2.10 on 2022-01-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='local_address_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Local address'),
        ),
        migrations.AddField(
            model_name='institution',
            name='local_address_ne',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Local address'),
        ),
    ]
