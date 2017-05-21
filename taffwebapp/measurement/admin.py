from django.contrib import admin

from measurement.models.measurement import measurement
from measurement.models.measurement_climatic import (
        climatic_SensorType,
        climatic_SensorTypeList,
        climatic_SensorMax,
        climatic_SensorValue,
        climatic_SensorName,
        climatic_MeasureValues,
        climatic_TestLoad,
        climatic_AmbientTemp,
        measurement_climatic,

)

# Register your models here.


admin.site.register(measurement)
admin.site.register(climatic_SensorType)
admin.site.register(climatic_SensorTypeList)
admin.site.register(climatic_SensorMax)
admin.site.register(climatic_SensorValue)
admin.site.register(climatic_SensorName)
admin.site.register(climatic_MeasureValues)
admin.site.register(climatic_TestLoad)
admin.site.register(climatic_AmbientTemp)
admin.site.register(measurement_climatic)
