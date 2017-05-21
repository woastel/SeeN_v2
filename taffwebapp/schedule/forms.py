from django import forms
from .models import (
    Schedule,
    ScheduleItem_Material,
    ScheduleItem_Measurement,
    ScheduleItem_Certification,
    Measurement_Type,
    Certification_Type )


class Create_Schedule_Form(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            "name",
            "info",
            "created_user",
            "creation_date",
            "system",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'creation_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }


class Create_CertificationType_Form(forms.ModelForm):
    class Meta:
        model = Certification_Type
        fields = [
            "name",
            "estimated_days",
        ]


class Create_ScheduleItemCertification_Form(forms.ModelForm):

    start_date_calculation = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )


    end_date_calculation = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

    class Meta:
        model = ScheduleItem_Certification
        fields = [
            "name",
            "info",
            "created_user",
            "creation_date",
            "delivery_date",
            "estimated_end_date",
            "certificatio_type",
            "schedule",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'creation_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'estimated_end_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }

    field_order = [
        "name",
        "info",
        "created_user",
        "creation_date",
        "delivery_date",
        "start_date_calculation",
        "estimated_end_date",
        "end_date_calculation",
        "measurement_type",
        "schedule",
        ]


class Create_MeasurementType_Form(forms.ModelForm):
    class Meta:
        model = Measurement_Type
        fields = [
            "name",
            "estimated_days",
        ]


class Create_ScheduleItemMeasurement_Form(forms.ModelForm):

    end_date_calculation = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

    class Meta:
        model = ScheduleItem_Measurement
        fields = [
            "name",
            "info",
            "created_user",
            "creation_date",
            "delivery_date",
            "estimated_end_date",
            "measurement_type",
            "schedule",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'creation_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'estimated_end_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }



    field_order = [
        "name",
        "info",
        "created_user",
        "creation_date",
        "delivery_date",
        "estimated_end_date",
        "end_date_calculation",
        "measurement_type",
        "schedule",
        ]


class Create_ScheduleItemMaterial_Form(forms.ModelForm):
    class Meta:
        model = ScheduleItem_Material
        fields = [
            "name",
            "info",
            "created_user",
            "creation_date",
            "delivery_date",
            "schedule",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'creation_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'delivery_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }
