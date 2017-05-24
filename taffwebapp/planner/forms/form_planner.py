from django import forms
from planner.models import planner



class Form_Create_PlannerSchedule(forms.ModelForm):
    class Meta:
        model = planner.schedule
        fields = [  'name',
                    'information',
                    'public',
            ]

class Form_Create_Schedule_System_Connection(forms.ModelForm):
    class Meta:
        model = planner.schedule_system_connection
        fields = [ 'system' ]

class Form_Create_Schedule_Component_Connection(forms.ModelForm):
    class Meta:
        model = planner.schedule_component_connection
        fields = [ 'component' ]
