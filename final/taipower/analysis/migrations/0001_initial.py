# Generated by Django 3.2 on 2021-06-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LatestThreeBackupHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('backup_volume', models.FloatField()),
                ('backup_volume_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PeakBackupThisYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('backup_volume', models.FloatField()),
                ('backup_volume_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PeakSupportDemandHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('peak_support', models.FloatField()),
                ('peak_demand', models.FloatField()),
                ('backup_volume', models.FloatField()),
                ('backup_volume_rate', models.FloatField()),
                ('industry', models.FloatField()),
                ('domestic', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerPlantSuppportHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('name', models.CharField(max_length=30)),
                ('support', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UsageByCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('big', models.CharField(max_length=100)),
                ('mid', models.CharField(max_length=100)),
                ('small', models.CharField(max_length=100)),
                ('usage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UsageStatisticHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('light_sale', models.FloatField()),
                ('power_sale', models.FloatField()),
                ('total_power_sale', models.FloatField()),
                ('light_number', models.FloatField()),
                ('power_number', models.FloatField()),
                ('total_number', models.FloatField()),
                ('non_business_light_number', models.FloatField()),
                ('business_light_number', models.FloatField()),
                ('mean_light_price', models.FloatField()),
                ('mean_power_price', models.FloatField()),
                ('total_mean_power_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ValueAdjustHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
