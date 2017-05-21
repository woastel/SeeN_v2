from django.contrib import admin
from .models import AmbientTemp, Climaticmeasure, MeasureValues, SensorMax
from .models import SensorName, SensorType, SensorTypeList, SensorValue
from .models import TestLoad
# Register your models here.
admin.site.register(AmbientTemp)
admin.site.register(Climaticmeasure)
admin.site.register(MeasureValues)
admin.site.register(SensorMax)
admin.site.register(SensorName)
admin.site.register(SensorType)
admin.site.register(SensorTypeList)
admin.site.register(SensorValue)
admin.site.register(TestLoad)
