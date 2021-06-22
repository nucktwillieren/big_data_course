from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'powerplant/history',
                PowerPlantSuppportHistoryViewSet, basename='analysis')
router.register(r'backup/history',
                PeakBackupHistoryViewSet, basename='analysis')
router.register(r'peak/history',
                PeakSupportDemandHistoryViewSet, basename='analysis')
router.register(r'peak/now', PeakBackupThisYearViewSet,
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
