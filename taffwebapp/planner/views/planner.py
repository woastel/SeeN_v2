from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
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
    form_class_create_schedule = form_planner.Form_Create_PlannerSchedule

    def get(self, request, *args, **kwargs):
        # Inital context for the render function
        context = {}
        context['panel_titel'] = self.panel_titel
        # add the forms to the context
        context['form_class_schedule_system_connection'] = self.form_class_schedule_system_connection
        context['form_class_schedule_component_connection'] = self.form_class_schedule_component_connection



        # get the schedule id from the kwargs
        schedule_id = kwargs["pk"]
        # get a schedule model by the schedule id
        scheduleItem_list = plannermodel.schedule.objects.filter(id=schedule_id)

        if len(scheduleItem_list) != 0:
            scheduleItem = scheduleItem_list[0]
            context['schedule_item'] = scheduleItem

            if scheduleItem.main_connection_avalible == False:
                messages.warning(request, '<b>Warning</b> Please add a Main Connection - a Main Connection is the first System or Component')
        else:
            messages.error(request, '<b>Error</b> no Schedule with id {} avalible'.format(schedule_id))

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

            # Checken ob es schon eine connection mit schedule_item und system gibt
            # dazu brauchen wir das object
            test_list = plannermodel.schedule_system_connection.objects.filter(schedule=schedule_item, system=instance.system)
            # wenn ja dann den vorgang abbrechen und einen fehler ausgeben
            if len(test_list) != 0:
                print("Dieses object gibt es schon ")
                messages.add_message(request, messages.ERROR, '<b>Error:</b> Diese Connection zwischen schedule {} und system {} gibt es schon'.format(schedule_item, instance.system))
                return redirect(reverse('planner:schedule_detail', kwargs={'pk': kwargs['pk']}))

            # checken ob schon eine main conection vorhandedn ist
            # wenn nicht das das object als mein connection setzen
            if schedule_item.main_connection_avalible == False:
                schedule_item.main_connection_avalible = True
                schedule_item.save()
                instance.is_a_main_connection = True

            # jetzt noch die instance speichern
            instance.save()
            # und eine info massage ausgeben
            messages.add_message(request, messages.INFO, '<b>INFO:</b> Adding System was successfully')
            return redirect(reverse('planner:schedule_detail', kwargs={'pk': kwargs['pk']}))

        if form_schedule_component_connection.is_valid():
            instance = form_schedule_component_connection.save(commit=False)
            instance.date_creation = datetime.now()
            instance.user_creation = request.user
            instance.schedule = schedule_item
            instance.is_a_main_connection = False

            # Checken ob es schon eine connection mit schedule_item und system gibt
            # dazu brauchen wir das object
            test_list = plannermodel.schedule_component_connection.objects.filter(schedule=schedule_item, component=instance.component)
            # wenn ja dann den vorgang abbrechen und einen fehler ausgeben
            if len(test_list) != 0:
                print("Dieses object gibt es schon ")
                messages.add_message(request, messages.ERROR, '<b>Error:</b> Diese Connection zwischen schedule {} und component {} gibt es schon'.format(schedule_item, instance.component))
                return redirect(reverse('planner:schedule_detail', kwargs={'pk': kwargs['pk']}))

            # checken ob schon eine main conection vorhandedn ist
            # wenn nicht das das object als mein connection setzen
            if schedule_item.main_connection_avalible == False:
                schedule_item.main_connection_avalible = True
                schedule_item.save()
                instance.is_a_main_connection = True

            instance.save()
            messages.add_message(request, messages.INFO, '<b>INFO:</b> Adding Component was successfully')
            return redirect(reverse('planner:schedule_detail', kwargs={'pk': kwargs['pk']}))

        return redirect(reverse('planner:schedule_detail', kwargs={'pk': kwargs['pk']}))
