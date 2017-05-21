from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    Create_System_Form,
    Create_Milestone_Form,
    Create_SystemModel_Form,
    Create_MSDBConnention_Form,
    Create_MSDBConnention_Form2,
    Create_Component_Connection_Form
)

from django.core.urlresolvers import reverse

from .models import (
    System,
    SystemModel,
    Milestone,
    MSDBConnention,
    System_Component_connection
)

from datetime import datetime




@method_decorator(login_required, name='dispatch')
class Main_View(View):

    template_name = "system/index.html"


    def get(self, request, *args, **kwargs):

        context = {}

        context["system_list"] = System.objects.all()
        context["system_model_list"] = SystemModel.objects.all()
        context["milestone_list"] = Milestone.objects.all()
        context["msdb_connection"] = MSDBConnention.objects.all()


        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class List_All_Systems(View):
    tempalteName = 'system/system_list_view.html'
    panel_titel = 'System List View'

    def get(self, request, *args, **kwargs):
        context = {}

        systemlist = System.objects.all()
        context['system_list'] = systemlist

        context['panel_titel'] = self.panel_titel

        return render(request, self.tempalteName, context)

@method_decorator(login_required, name='dispatch')
class Detail_System_View(View):
    templateName = 'system/system_detail_view.html'
    panel_titel = 'System Detail View'

    def get(self, request, *args, **kwargs):
        context = {}

        # system id aus den kwargs holen
        var_system_id = kwargs["pk"]

        # geht the systemobject by the id
        var_system_obj_list = System.objects.filter(id=var_system_id)

        # wenn die liste leer ist dann gibt es das gesuchte object nicht
        #   jetzt kann eine warnung ausgegeben werden
        if len(var_system_obj_list) != 0:
            # catch the systemobject
            var_system = var_system_obj_list[0]
            # add the system to context
            context['system'] = var_system
            # get the hole list of msdb connections from the system
            msdbconnection_list = MSDBConnention.objects.filter(system=var_system).order_by('milestone__name')
            context['msdbconnection_list'] = msdbconnection_list


            system_component_connection_list = (
                System_Component_connection.objects.filter(
                    system=var_system).order_by('component__component_id'))

            context['system_component_connection_list'] = (
                system_component_connection_list)

        else:
            # warning output
            print("Error: the system is not avalible")

        # add the panel titel
        context['panel_titel'] = self.panel_titel

        # and render the page
        return render(request, self.templateName, context)





@method_decorator(login_required, name='dispatch')
class Create_System_View(View):
    form_class = Create_System_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a System'}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            ## instance.created_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

class Update_System_View(UpdateView):
    form_class = Create_System_Form
    model = System
    template_name = 'system/system_createForm.html'
    success_url = reverse_lazy('system:system_index')

class Delete_System_View(DeleteView):
    model = System
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy('system:system_index')




@method_decorator(login_required, name='dispatch')
class Create_SystemModel_View(View):
    form_class = Create_SystemModel_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a System Model'}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            ## instance.created_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class Create_Milestone_View(View):
    form_class = Create_Milestone_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a Milestone'}

    def get(self, request, *args, **kwargs):

        initial = {
            "creator": request.user,
            "createtion_date": datetime.now(),
        }

        form = self.form_class(initial=initial)
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            instance.creator = request.user
            instance.createtion_date = datetime.now()

            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)




# Create MSDB Connections
#   1. Free View ( you can select a system and a milestone )
#   2. From Systemside ( you can only select a milstone )

@method_decorator(login_required, name='dispatch')
class Create_MSDBConnection_View(View):
    form_class = Create_MSDBConnention_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a Milestone Time System Connection'}

    def get(self, request, *args, **kwargs):

        initial = {
            "creator": request.user,
            "creation_date": datetime.now(),
        }

        form = self.form_class(initial=initial)
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        # laden der ausgefuellten form aus dem POST request
        form = self.form_class(request.POST)

        print("---------------------")
        print("-- DEBUG           --")
        print("---------------------")
        print("---------------------")

        # Die System id aus dem POST request laden
        system_id = request.POST["system"]
        # die milestone id aus dem POST request laden
        milestone_id = request.POST["milestone"]

        print(system_id)
        print(milestone_id)
        print("---------------------")


        # Alle Objecte laden die system_id und milestone_id enthalten
        # Denn es darf für jedes system nur ein milesone mit einem type geben
        # nicht das es 2x den MS 10 gibt
        list_msdb_connects = MSDBConnention.objects.filter( system=system_id,
                                                            milestone=milestone_id)
        print("---------------------")
        print(list_msdb_connects)
        print("Anzahl objects vorhanden: {}".format(len(list_msdb_connects)))
        print("---------------------")

        # checken ob die geladene liste objecte enthaelt
        # oder die laenge der liste 0 ist
        if len(list_msdb_connects) != 0:
            error_msg = []
            error_msg.append(str("Es besteht schon ein objekt aus system_id {} und milestone_id {}".format(system_id, milestone_id)))
            print("DEBUG: Error: es ist schon ein Objects dieser Kombination vorhanden")

        else:
            print("DEBUG: OK: Object kann erstellt werden.")

            if form.is_valid():

                instance = form.save(commit=False)

                # Hier kann das instance object nochmal geaendert werden
                ## instance.created_user = request.user

                instance.creator = request.user
                instance.creation_date = datetime.now()

                # hier kann sollte noch ueberprueft werden ob
                #   das datum des Milestone Finish date groeser ist als das datum
                #    der erstellung

                instance.save()
                return HttpResponseRedirect(reverse('system:system_index'))


        context = {'form': form}
        context.update(self.panel_titel)
        context.update({"error_msg_avalible": True})
        context.update({"error_msg_list": error_msg})
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Create_MSDB_Connection_from_system(View):
    form_class = Create_MSDBConnention_Form2
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a Milestone Time System Connection'}


    def get(self, request, *args, **kwargs):


        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        # laden der ausgefuellten form aus dem POST request
        form = self.form_class(request.POST)


        # Die System id aus dem POST request laden
        print(kwargs)
        system_id = kwargs["pk"]
        # die milestone id aus dem POST request laden
        milestone_id = request.POST["milestone"]



        # Alle Objecte laden die system_id und milestone_id enthalten
        # Denn es darf für jedes system nur ein milesone mit einem type geben
        # nicht das es 2x den MS 10 gibt
        list_msdb_connects = MSDBConnention.objects.filter( system=system_id,
                                                            milestone=milestone_id)

        # checken ob die geladene liste objecte enthaelt
        # oder die laenge der liste 0 ist
        if len(list_msdb_connects) != 0:
            error_msg = []
            error_msg.append(str("Es besteht schon ein objekt aus system_id {} und milestone_id {}".format(system_id, milestone_id)))
            print("DEBUG: Error: es ist schon ein Objects dieser Kombination vorhanden")

        else:
            print("DEBUG: OK: Object kann erstellt werden.")

            if form.is_valid():

                instance = form.save(commit=False)

                instance.creator = request.user
                instance.creation_date = datetime.now()
                system_var = System.objects.filter(id=system_id)[0]
                instance.system = system_var

                instance.save()
                return HttpResponseRedirect(reverse_lazy('system:system_detail', kwargs={"pk": system_id}))


        context = {'form': form}
        context.update(self.panel_titel)
        context.update({"error_msg_avalible": True})
        context.update({"error_msg_list": error_msg})
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Delete_MSDB_Connection(DeleteView):
    model = MSDBConnention
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy('system:system_index')


    def delete(self, request, *args, **kwargs):
        """
            Funktion to check the user
            only the creator can delete the object nobody else
        """

        # get the object you would be delete
        self.object = self.get_object()
        # check if the creator.username is the requested username
        ## if self.object.creator.username != request.user.get_username():
        ##     # if not send a error
        ##     return HttpResponse("FAIL not the right user")

        print(kwargs)

        system = self.object.system

        self.success_url = reverse_lazy('system:system_detail', kwargs={"pk": system.id})

        # store the success url
        success_url = self.get_success_url()
        # delete the object
        self.object.delete()
        # return the success url
        return HttpResponseRedirect(success_url)


# Views for the System - Component Conection
@method_decorator(login_required, name='dispatch')
class Create_Component_Connection(View):
    form_class = Create_Component_Connection_Form
    template_name = 'system/system_createForm.html'
    panel_titel = 'Create a Milestone Time System Connection'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {}
        context["form"] = form
        context["panel_titel"] = self.panel_titel

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # laden der ausgefuellten form aus dem POST request
        form = self.form_class(request.POST)


        # Die System id aus dem POST request laden
        print(kwargs)
        system_id = kwargs["pk"]
        # die milestone id aus dem POST request laden
        component_id = request.POST["component"]



        # Alle Objecte laden die system_id und milestone_id enthalten
        # Denn es darf für jedes system nur ein milesone mit einem type geben
        # nicht das es 2x den MS 10 gibt
        list_component_connects = System_Component_connection.objects.filter(
                                        system=system_id, component=component_id)

        # checken ob die geladene liste objecte enthaelt
        # oder die laenge der liste 0 ist
        if len(list_component_connects) != 0:
            error_msg = []
            error_msg.append(str("Es besteht schon ein objekt aus system_id {} und component_id {}".format(system_id, component_id)))
            print("DEBUG: Error: es ist schon ein Objects dieser Kombination vorhanden")

        else:
            print("DEBUG: OK: Object kann erstellt werden.")

            if form.is_valid():

                instance = form.save(commit=False)

                instance.user_creator = request.user
                instance.date_creation = datetime.now()
                system_var = System.objects.filter(id=system_id)[0]
                instance.system = system_var

                instance.save()
                return HttpResponseRedirect(reverse_lazy('system:system_detail', kwargs={"pk": system_id}))


        context = {'form': form}
        context["panel_titel"] = self.panel_titel
        context.update({"error_msg_avalible": True})
        context.update({"error_msg_list": error_msg})
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Delete_Component_Connection(DeleteView):
    model = System_Component_connection
    template_name = "components/component_delete_confirm.html"

    def delete(self, request, *args, **kwargs):
        """
            Funktion to check the user
            only the creator can delete the object nobody else
        """

        # get the object you would be delete
        self.object = self.get_object()
        # check if the creator.username is the requested username
        ## if self.object.creator.username != request.user.get_username():
        ##     # if not send a error
        ##     return HttpResponse("FAIL not the right user")

        print(kwargs)

        system = self.object.system

        self.success_url = reverse_lazy('system:system_detail', kwargs={"pk": system.id})

        # store the success url
        success_url = self.get_success_url()
        # delete the object
        self.object.delete()
        # return the success url
        return HttpResponseRedirect(success_url)
