from django.contrib import admin

from .models import (
    Schedule,
    Certification_Type,
    ScheduleItem_Certification,
    Measurement_Type,
    ScheduleItem_Measurement,
    ScheduleItem_Material)

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Certification_Type)
admin.site.register(ScheduleItem_Certification)
admin.site.register(Measurement_Type)
admin.site.register(ScheduleItem_Measurement)
admin.site.register(ScheduleItem_Material)
