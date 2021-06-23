from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'powerplant',
                PowerPlantSuppportHistoryViewSet, basename='analysis')
router.register(r'peak/detail',
                PeakSupportDemandHistoryViewSet, basename='analysis')
router.register(r'peak/yearly',
                YearlyPeakBackupHistoryViewSet, basename='analysis')
router.register(r'peak/daily', DailyPeakBackupViewSet,
                basename='analysis')
router.register(r'usage/history',
                UsageStatisticHistoryViewSet, basename='analysis')
router.register(r'usage/category', UsageByCategoryViewSet,
                basename='analysis')
router.register(r'neighborhood', NeighborhoodViewSet, basename='analysis')
router.register(r'price/adjust/history',
                PriceAdjustHistoryViewSet, basename='analysis')

urlpatterns = [

] + router.urls
