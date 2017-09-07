from django import forms

from milestones.models import milestone

class Form_Create_milestone(forms.ModelForm):
    class Meta:
        model = milestone
        fields = '__all__'

        widgets = {
            'date_creation': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            'date_update': forms.DateTimeInput(
                            attrs={'class': 'datetime-input'}),
            }
