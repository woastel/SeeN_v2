from django.views import generic, View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.db.models import Q

from milestones.forms import form_milestones
from eut.models import Eut


class IndexView(generic.View):
    template_name = 'milestones/index_.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class Create_Milestone(View):
    form_class = form_milestones.Form_Create_milestone
    template_name = 'measurement/formular.html'
    panel_titel = 'Add a Ambient Temperature'

    def get(self, request, *args, **kwargs):
        context = {}
        initial = {}

        form = self.form_class(initial=initial)

        context = {'form': form}
        context["panel_titel"] = self.panel_titel
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('measurement:mc_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)
