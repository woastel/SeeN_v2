from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime

from planner.forms import form_planner

from planner.models import planner as plannermodel



class IndexView(generic.View):
    template_name = 'planner/index_.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)


class CreateSchedule(generic.View):
    form_class = form_planner.Form_Create_PlannerSchedule
    template_name = 'planner/create_schedule_form.html'
    panel_titel = 'Create Schedule Formular'

    def get(self, request, *args, **kwargs):
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        print(request.POST)
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creation = request.user
            instance.user_update = request.user
            instance.main_connection_avalible = False

            instance.save()

            return HttpResponseRedirect(reverse('planner:index'))

        context = {'form': form}
        context["panel_titel"] = self.panel_titel
        return render(request, self.template_name, context)


class ScheduleListView(generic.View):
    template_name = 'planner/schedule_list.html'
    panel_titel = 'List of all Schedules'


    def get(self, request, *args, **kwargs):
        context = {}

        # get the list of all schedules
        scheduleList = plannermodel.schedule.objects.all()

        context['schedule_list'] = scheduleList

        context['panel_titel'] = self.panel_titel

        return render(request, self.template_name, context)

class ScheduleDetailView(generic.View):
    template_name = 'planner/schedule_detail_view.html'
    panel_titel = 'Detail View of a Schedule'
    form_class_schedule_system_connection = form_planner.Form_Create_Schedule_System_Connection
    form_class_schedule_component_connection = form_planner.Form_Create_Schedule_Component_Connection

    def get(self, request, *args, **kwargs):
        # Inital context for the render function

        context = {}
        context['panel_titel'] = self.panel_titel
        # add the forms to the context
        context['form_class_schedule_system_connection'] = self.form_class_schedule_system_connection
        context['form_class_schedule_component_connection'] = self.form_class_schedule_component_connection
        # Set the Alert Variables to False (default)
        context['alert_success_avalible'] = False
        context['alert_success'] = ""
        context['alert_warning_avalible'] = False
        context['alert_warning'] = ""
        context['alert_danger_avalible'] = False
        context['alert_danger'] = ""

        print("KW in get method")
        print(kwargs)


        # get the schedule id from the kwargs
        schedule_id = kwargs["pk"]
        # get a schedule model by the schedule id
        scheduleItem_list = plannermodel.schedule.objects.filter(id=schedule_id)

        if len(scheduleItem_list) != 0:
            scheduleItem = scheduleItem_list[0]
            context['schedule_item'] = scheduleItem

            if scheduleItem.main_connection_avalible == False:

                context['alert_warning_avalible'] = True
                context['alert_warning'] = str("Es wurde nicht keine Main Connection ausgewählt bitte erstellen sie eine")

            if "danger" in kwargs:
                context['alert_danger_avalible'] = True
                context['alert_danger'] += str('Error - {}'.format(kwargs["danger"]))


            if "success" in kwargs:
                context['alert_success_avalible'] = True
                context['alert_success'] += str('Success - {}'.format(kwargs["success"]))

            context['alert_success_avalible'] = True
            context['alert_success'] += str('Pass - Component with id({}) is avalible.'.format(schedule_id))

        else:
            context['alert_danger_avalible'] = True
            context['alert_danger'] += str('<p>Error - Component with id({}) isnt avalible.</p>'.format(schedule_id))

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        context['panel_titel'] = self.panel_titel
        context['form_class_schedule_system_connection'] = self.form_class_schedule_system_connection
        context['form_class_schedule_component_connection'] = self.form_class_schedule_component_connection

        form_schedule_system_connection = self.form_class_schedule_system_connection(request.POST)
        form_schedule_component_connection = self.form_class_schedule_component_connection(request.POST)

        schedule_item = plannermodel.schedule.objects.filter(pk=kwargs['pk'])[0]

        if form_schedule_system_connection.is_valid():
            instance = form_schedule_system_connection.save(commit=False)
            instance.date_creation = datetime.now()
            instance.user_creation = request.user
            instance.schedule = schedule_item
            instance.is_a_main_connection = False

            if schedule_item.main_connection_avalible == False:
                schedule_item.main_connection_avalible = True
                schedule_item.save()
                instance.is_a_main_connection = True


            instance.save()
            return redirect(reverse('planner:schedule_detail_with_success', kwargs={'pk': kwargs['pk'], 'success': "asdf"}))

        if form_schedule_component_connection.is_valid():
            instance = form_schedule_component_connection.save(commit=False)
            instance.date_creation = datetime.now()
            instance.user_creation = request.user
            instance.schedule = schedule_item
            instance.is_a_main_connection = False

            if schedule_item.main_connection_avalible == False:
                schedule_item.main_connection_avalible = True
                schedule_item.save()
                instance.is_a_main_connection = True

            instance.save()
            return redirect(reverse('planner:schedule_detail_with_success', kwargs={'pk': kwargs['pk'], 'success': "component_added"}))



        return redirect(reverse('planner:schedule_detail_with_danger', kwargs={'pk': kwargs['pk'], 'danger': "Cant_added"}))
