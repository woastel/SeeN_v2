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

class Form_Create_Schedule_Item(forms.ModelForm):
    class Meta:
        model = planner.scheduleItem
        fields = [  'name',
                    'item_start_date_avalible',
                    'item_start_date',
                    'item_end_date_avalible',
                    'item_end_date',
                    'item_duration_avalible',
                    'item_duration',
                    'item_dependencies_avalible']

        widgets = {
                    'item_start_date': forms.DateTimeInput(attrs={'class':'datetime-input'}),
                    'item_end_date': forms.DateTimeInput(attrs={'class':'datetime-input'}),

                    }

class Form_Update_Schedule_Public(forms.ModelForm):
    class Meta:
        model = planner.schedule
        fields = [  'public']
