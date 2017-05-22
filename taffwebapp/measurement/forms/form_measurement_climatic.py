from django import forms
from measurement.models.measurement_climatic import measurement_climatic
from measurement.models.measurement_climatic import (
        climatic_TestLoad,
        climatic_AmbientTemp,
        climatic_SensorTypeList
)

from components.models import Component

class Form_Create_AmbientTemperature(forms.ModelForm):
    class Meta:
        model = climatic_AmbientTemp
        fields = '__all__'

class Form_Create_TestLoad(forms.ModelForm):
    class Meta:
        model = climatic_TestLoad
        fields = '__all__'

class Form_Create_SensorTypeList(forms.ModelForm):

    typee1  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee2  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee3  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee4  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee5  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee6  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee7  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee8  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee9  = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee10 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee11 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee12 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee13 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee14 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee15 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee16 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee17 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee18 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee19 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee20 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee21 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee22 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee23 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee24 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee25 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee26 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee27 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee28 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee29 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee30 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee31 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee32 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee33 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee34 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee35 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee36 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee37 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee38 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee39 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee40 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee41 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee42 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee43 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee44 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee45 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee46 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee47 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee48 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee49 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee50 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee51 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee52 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee53 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee54 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee55 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee56 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee57 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee58 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee59 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    typee60 = forms.ModelChoiceField(queryset=Component.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)

    class Meta:
        model = climatic_SensorTypeList
        fields = '__all__'

class UploadFileForm(forms.ModelForm):
    # sensorTypeList  = forms.ModelChoiceField(queryset=climatic_SensorTypeList.objects.filter(character_thermal_avalible=True).order_by("component_type_text"), empty_label="(Nothing)", required=False)
    _file = forms.FileField()

    class Meta:
        model = measurement_climatic
        fields = [
            "name",
            "information",
            "date_creation",
            "date_update",
            "user_creation",
            "user_update",

            "eut",
            "measurement_is_pass",
            "measurement_is_public",
            
            "AmbientTemp",
            "TestLoad",
            "sensortypeList_avalible",
            "sensorTypeList",

        ]

        widgets = {
            'date_creation': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            'date_update': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            }
