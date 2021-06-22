from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.


class PowerPlantSuppportHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlantSuppportHistory
        fields = '__all__'


class PeakBackupHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakBackupHistory
        fields = '__all__'


class PeakSupportDemandHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakSupportDemandHistory
        fields = '__all__'


class PeakBackupThisYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakBackupThisYear
        fields = '__all__'


class UsageStatisticHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageStatisticHistory
        fields = '__all__'


class UsageByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageByCategory
        fields = '__all__'


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class PriceAdjustHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAdjustHistory
        fields = '__all__'
