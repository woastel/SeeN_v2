from django.contrib import admin
from .models import (
    Vendor,
    #Component_Type,
    Component,
    Component_Character_Thermal,
    Component_Character_Mechanical,
    Component_Character_Electrical_Power,
    Chassis,
    ChassisAddOn,
    Motherboard,
    Cpu,
    Memory,
    PSU,
    HDD,
    HeatSink,
    Fan,
    Cable,
    Pcba,
    Pcie_Ctrl
)
# Register your models here.


admin.site.register(Vendor)
#admin.site.register(Component_Type)
admin.site.register(Component)
#admin.site.register(Component_Character_Mechanical)
#admin.site.register(Component_Character_Electrical_Power)
#admin.site.register(Component_Character_Thermal)
admin.site.register(Chassis)
admin.site.register(ChassisAddOn)
admin.site.register(Motherboard)
admin.site.register(Cpu)
admin.site.register(Memory)
admin.site.register(PSU)
admin.site.register(HDD)
admin.site.register(HeatSink)
admin.site.register(Fan)
admin.site.register(Cable)
admin.site.register(Pcba)
admin.site.register(Pcie_Ctrl)
