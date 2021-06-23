from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PowerPlantSuppportHistory)
admin.site.register(YearlyPeakBackupHistory)
admin.site.register(PeakSupportDemandHistory)
admin.site.register(PeakBackupThisYear)
admin.site.register(UsageStatisticHistory)
admin.site.register(UsageByCategory)
admin.site.register(Neighborhood)
admin.site.register(PriceAdjustHistory)
