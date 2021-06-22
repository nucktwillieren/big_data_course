from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import mixins
from .plot import *


class CreateListModelMixin(object):
    pass
    # def get_serializer(self, *args, **kwargs):
    #    """ if an array is passed, set serializer to many """
    #    if isinstance(kwargs.get('data', {}), list):
    #        kwargs['many'] = True
    #    return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PowerPlantSuppportHistoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = PowerPlantSuppportHistory.objects.all()
    serializer_class = PowerPlantSuppportHistorySerializer


class PeakBackupHistoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = PeakBackupHistory.objects.all()
    serializer_class = PeakBackupHistorySerializer


class PeakSupportDemandHistoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = PeakSupportDemandHistory.objects.all()
    serializer_class = PeakSupportDemandHistorySerializer


class PeakBackupThisYearViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = PeakBackupThisYear.objects.all()
    serializer_class = PeakBackupThisYearSerializer


class UsageStatisticHistoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = UsageStatisticHistory.objects.all()
    serializer_class = UsageStatisticHistorySerializer


class UsageByCategoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = UsageByCategory.objects.all()
    serializer_class = UsageByCategorySerializer


class NeighborhoodViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer


class PriceAdjustHistoryViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = PriceAdjustHistory.objects.all()
    serializer_class = PriceAdjustHistorySerializer


class AnalysisPage(TemplateView):
    template_name = "analysis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['graph'] = example_graph()

        return context
