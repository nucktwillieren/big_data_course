# Generated by Django 3.2 on 2021-06-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_auto_20210623_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peaksupportdemandhistory',
            name='powerplant',
            field=models.ManyToManyField(blank=True, to='analysis.PowerPlantSuppportHistory'),
        ),
    ]
