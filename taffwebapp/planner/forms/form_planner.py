from django import forms
from planner.models import planner



class Form_Create_PlannerSchedule(forms.ModelForm):
    class Meta:
        model = planner.schedule
        fields = [  'name',
                    'information',
                    'public',
            ]
