# Generated by Django 3.2 on 2021-06-23 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_alter_peaksupportdemandhistory_powerplant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peaksupportdemandhistory',
            name='powerplant',
        ),
    ]