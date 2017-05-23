from django.views import generic
from django.shortcuts import render
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

    def get(self, request, *args, **kwargs):
        context = {}

        schedule_id = kwargs["pk"]

        scheduleItem = plannermodel.schedule.objects.filter(id=schedule_id)

        if len(scheduleItem) != 0:
            context['schedule_item'] = scheduleItem[0]

        context['panel_titel'] = self.panel_titel

        return render(request, self.template_name, context)
