from django import forms
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


# Forms for types this schould only use by the admin
class Form_Vendor(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

#class Form_Component_Type(forms.ModelForm):
#    class Meta:
#        model = Component_Type
#        fields = '__all__'


# general Forms from the components models
class Form_Chassis(forms.ModelForm):
    class Meta:
        model = Chassis
        #fields = '__all__'
        exclude = [ 'component_type_text',
                    'date_creation',
                    'date_update',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_ChassisAddOn(forms.ModelForm):
    class Meta:
        model = ChassisAddOn
        exclude = [ 'component_type_text',
                    'date_creation',
                    'date_update',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Motherboard(forms.ModelForm):
    class Meta:
        model = Motherboard
        exclude = [ 'date_creation',
                    'component_type_text',
                    'date_update',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Cpu(forms.ModelForm):
    class Meta:
        model = Cpu
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Memory(forms.ModelForm):
    class Meta:
        model = Memory
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_PSU(forms.ModelForm):
    class Meta:
        model = PSU
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_HDD(forms.ModelForm):
    class Meta:
        model = HDD
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_HeatSink(forms.ModelForm):
    class Meta:
        model = HeatSink
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Fan(forms.ModelForm):
    class Meta:
        model = Fan
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Cable(forms.ModelForm):
    class Meta:
        model = Cable
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}

class Form_Pcba(forms.ModelForm):
    class Meta:
        model = Pcba
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}


class Form_Pcie_Ctrl(forms.ModelForm):
    class Meta:
        model = Pcie_Ctrl
        exclude = [ 'date_creation',
                    'date_update',
                    'component_type_text',
                    'user_creator',
                    'user_updater',
                    'character_mechanical_avalible',
                    'character_electrical_avalible',
                    'character_thermal_avalible']

        widgets = {
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'})}
