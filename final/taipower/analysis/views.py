from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import TemplateView
from .plot import *


class PowerPlantSuppportHistoryViewSet(viewsets.ModelViewSet):
    queryset = PowerPlantSuppportHistory.objects.all()
    serializer_class = PowerPlantSuppportHistorySerializer


class PeakBackupHistoryViewSet(viewsets.ModelViewSet):
    queryset = PeakBackupHistory.objects.all()
    serializer_class = PeakBackupHistorySerializer


class PeakSupportDemandHistoryViewSet(viewsets.ModelViewSet):
    queryset = PeakSupportDemandHistory.objects.all()
    serializer_class = PeakSupportDemandHistorySerializer


class PeakBackupThisYearViewSet(viewsets.ModelViewSet):
    queryset = PeakBackupThisYear.objects.all()
    serializer_class = PeakBackupThisYearSerializer


class UsageStatisticHistoryViewSet(viewsets.ModelViewSet):
    queryset = UsageStatisticHistory.objects.all()
    serializer_class = UsageStatisticHistorySerializer


class UsageByCategoryViewSet(viewsets.ModelViewSet):
    queryset = UsageByCategory.objects.all()
    serializer_class = UsageByCategorySerializer


class NeighborhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class PriceAdjustHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceAdjustHistory.objects.all()
    serializer_class = PriceAdjustHistorySerializer


class AnalysisPage(TemplateView):
    template_name = "analysis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['graph'] = example_graph()

        return context
