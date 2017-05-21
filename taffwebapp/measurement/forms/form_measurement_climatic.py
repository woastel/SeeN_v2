from django import forms
from measurement.models.measurement_climatic import measurement_climatic


class UploadFileForm(forms.ModelForm):
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

            "AmbientTemp",
            "TestLoad",
            "sensorTypeList",
        ]

        widgets = {
            'date_creation': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            'date_update': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            }
