from django import forms
from .models import Climaticmeasure



class UploadFileForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Climaticmeasure
        fields = [
            "name",
            "info",
            "creation_date",
            "creator",
            "eut_id_fk",
            "sensorTypeList_id_fk",
            # -- Dieses object wird noch erzeugt anahand des hochgeladenen files
            # "measureValues_id_fk",
            "testload_id_fk",
            "ambient_id_fk",
        ]

        widgets = {
            'creation_date': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
        }

    field_order = [
        "name",
        "info",
        "creator",
        "creation_date",
        "ambient_id_fk",
        "testload_id_fk",
        "eut_id_fk",
        "sensorTypeList_id_fk",
        # -- Dieses object wird noch erzeugt anahand des hochgeladenen files
        # "measureValues_id_fk",
        ]
