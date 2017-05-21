from django import forms

from .models import Todo


class ToDoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = [
            "name",
            "text",
            "priorityLevel",
            "createtion_date",
            # "creator", -- soll in der form nicht veraendert werden duerfen
            "must_done_date",
            "public",
            # "status_done"
        ]

        # widgets aendern
        # damit die call datetime-input ist damit mann die bootstrap datime
        # input verwendne kann
        widgets = {
            'createtion_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'must_done_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }
