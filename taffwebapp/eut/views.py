from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from system.models import System
from .models import Eut, Component_connection
from django.utils.decorators import method_decorator
from datetime import datetime
from .forms import Form_Eut, Form_Eut_component_connection

@method_decorator(login_required, name='dispatch')
class Eut_MainView(View):
    template_name = 'eut/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Eut_Create_view(View):
    form_class = Form_Eut
    template_name = 'eut/eut_create.html'

    def get(self, request, *args, **kwargs):
        context = {}
        initial = {
            "user_creator" : request.user,
            "user_updater" : request.user,
            "date_creation" : datetime.now(),
            "date_updateed" : datetime.now(),}

        form = self.form_class(initial=initial)
        context.update({'form': form})
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)


        if form.is_valid():
            form = form.save(commit=False)
            form.created_user = request.user
            form.save()

            return HttpResponseRedirect(reverse('eut:eut_detail' , kwargs={'pk': form.pk}))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Eut_list_view(View):
    template_name = 'eut/eut_list.html'

    def get(self, request, *args, **kwargs):
        context = {}

        eutlist = Eut.objects.all()
        context["eutlist"] = reversed(eutlist)

        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Eut_detail_view(View):
    form_add_component_class = Form_Eut_component_connection
    template_name = 'eut/eut_detail.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context["alert_danger_avalible"] = False

        # only debug information print
        print("kwargs: {}".format(kwargs))

        # store the pk of the request objects
        eut_id = kwargs["pk"]
        print(eut_id)
        # get the eut list
        eut = Eut.objects.filter(id=eut_id)

        initial = {"eut" : eut[0],}
        form = self.form_add_component_class(initial=initial)
        context["form"] = form

        for a in form:
            print(type(a))


        # get the eut list
        eut = Eut.objects.filter(id=eut_id)
        try:
            context["eut"] = eut[0]
        except:
            context["alert_danger_avalible"] = True
            context["alert_danger"] = str("EUT List query list is empty. " +
                                        "Eut with id {} is not avalible".format(eut_id))


        component_connection_list = Component_connection.objects.filter(eut=eut_id)
        print(component_connection_list)
        try:
            context["component_connection_list"] = component_connection_list
        except:
            context["alert_danger_avalible"] = True
            context["alert_danger"] = str("component conni is not avalible")



        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        """
            Diese POST Methode wird benötigit um einem EUT eine Component
            hinzuzufuegen.
        """
        form = self.form_add_component_class(request.POST)

        print("......................")
        print("kwargs")
        print(kwargs)
        print("......................")

        # eut_id aus den kwargs laden
        # diese eut id brauchen wir spaeter um dem component connection object
        # einen eut hinzuzufuegen
        eut_id = kwargs["pk"]

        if form.is_valid():
            form = form.save(commit=False)
            form.user_creator = request.user
            form.date_creation = datetime.now()
            form.eut = Eut.objects.filter(id=eut_id)[0]

            print("Das ist ein DEBUG")
            print("")
            print("")
            print(type(form))
            print("")
            print("")

            # save the form (object)
            form.save()


            return HttpResponseRedirect(reverse('eut:eut_detail', kwargs={"pk": form.eut.id}))

        context = {'form': form}

        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class DeleteComponentEutConnection(generic.DeleteView):
    model = Component_connection
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("eut:index")
