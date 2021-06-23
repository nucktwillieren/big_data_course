from django.db import models

# Create your models here.


class PowerPlantSuppportHistory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    name = models.CharField(max_length=30)
    support = models.FloatField()


class PeakSupportDemandHistory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    peak_support = models.FloatField()
    peak_demand = models.FloatField()
    backup_volume = models.FloatField()
    backup_volume_rate = models.FloatField()
    industry = models.FloatField()
    domestic = models.FloatField()
    powerplant = models.ManyToManyField(PowerPlantSuppportHistory, blank=True)


class PeakBackupHistory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    backup_volume = models.FloatField()
    backup_volume_rate = models.FloatField()


class PeakBackupThisYear(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    backup_volume = models.FloatField()
    backup_volume_rate = models.FloatField()


class UsageStatisticHistory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    light_sale = models.FloatField()
    power_sale = models.FloatField()
    total_power_sale = models.FloatField()
    light_number = models.FloatField()
    power_number = models.FloatField()
    total_number = models.FloatField()
    non_business_light_number = models.FloatField()
    business_light_number = models.FloatField()
    mean_light_price = models.FloatField()
    mean_power_price = models.FloatField()
    total_mean_power_price = models.FloatField()


class UsageByCategory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    big = models.CharField(max_length=100)
    mid = models.CharField(max_length=100)
    small = models.CharField(max_length=100)
    usage = models.FloatField()


class UsageByLocation(models.Model):
    pass


class Neighborhood(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    location = models.CharField(max_length=100)
    price = models.FloatField()


class PriceAdjustHistory(models.Model):
    time = models.DateTimeField(unique=True, db_index=True)
    name = models.CharField(max_length=100)
