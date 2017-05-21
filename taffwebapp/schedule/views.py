from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import (
    Create_Schedule_Form,
    Create_CertificationType_Form,
    Create_ScheduleItemCertification_Form,
    Create_MeasurementType_Form,
    Create_ScheduleItemMeasurement_Form,
    Create_ScheduleItemMaterial_Form)
from .models import (
    Schedule,
    ScheduleItem_Material,
    ScheduleItem_Measurement,
    ScheduleItem_Certification,
    Measurement_Type,
    Certification_Type)
from system.models import Milestone, MSDBConnention
from datetime import datetime
import datetime as datetimelib
from django.core.urlresolvers import reverse
import json


@method_decorator(login_required, name='dispatch')
class MainView(View):
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):

        username_request = self.request.user.username
        schedule_list = Schedule.objects.filter(created_user__username=username_request)
        context = {'schedule_list': reversed(schedule_list)}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Create_Schedule_View(View):
    form_class = Create_Schedule_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Create Schedule"}
    # title = "Create Schedule"
    def get(self, request, *args, **kwargs):

        initial = {
            "created_user" : request.user,
            "creation_date" : datetime.now(),
        }

        form = self.form_class(initial=initial)
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('schedule:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Schedule_View(UpdateView):
    model = Schedule
    form_class = Create_Schedule_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Schedule"}
    info_text = {"info_text": "Update Formular - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Schedule_View, self).get_context_data(**kwargs)
        # jetzt noch den titel hinzufügen
        context.update(self.panel_titel)
        context.update(self.info_text)
        # den context zuruek geben
        return context

@method_decorator(login_required, name='dispatch')
class Delete_Schedule_View(DeleteView):
    model = Schedule
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Schedule"}
    info_text = {"info_text": "Delete this Schedule - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_Schedule_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Create_CertificationType_View(View):
    form_class = Create_CertificationType_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Create Certification Type"}
    # title = "Create Schedule"
    def get(self, request, *args, **kwargs):

        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.created_user = request.user
            # instance.save()
            form.save()
            return HttpResponseRedirect(reverse('schedule:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_CertificationType_View(UpdateView):
    model = Certification_Type
    form_class = Create_CertificationType_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Certification Type"}
    info_text = {"info_text": "Delete this Certification Type - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Update_CertificationType_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Delete_CertificationType_View(DeleteView):
    model = ScheduleItem_Certification
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Certification Type"}
    info_text = {"info_text": "Delete this Certification Type - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_CertificationType_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Create_ScheduleItemCertification_View(View):
    form_class = Create_ScheduleItemCertification_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Create Schedule Item Certification"}
    # title = "Create Schedule"
    def get(self, request, *args, **kwargs):

        initial = {
            "created_user" : request.user,
            "creation_date" : datetime.now(),
        }

        form = self.form_class(initial=initial)
        username_request = self.request.user.username
        form.fields["schedule"].queryset = Schedule.objects.filter(
            created_user__username=username_request)
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        schould_generate_delivery_date = request.POST["start_date_calculation"]
        schould_generate_end_date = request.POST["end_date_calculation"]

        print("------------------")
        print(schould_generate_delivery_date)
        print(schould_generate_end_date)
        print("------------------")

        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user

            if schould_generate_end_date == "True":
                print("End date generetion: True")
                # laden des MS70 datums
                system_id_temp = instance.schedule.system.id
                queryset_object_list = MSDBConnention.objects.filter(
                                            system__id=system_id_temp,
                                            milestone__name="MS70")
                # Jetzt muss das erste objekt aus der list geholt werden
                msdbconnection_object = queryset_object_list[0]

                print(msdbconnection_object.milestoneFinish_date)
                instance.estimated_end_date = msdbconnection_object.milestoneFinish_date

            elif schould_generate_end_date == "False":
                print("End date generetion: False")
                pass

            if schould_generate_delivery_date == "True":
                print("Delivery date generetion: True")

                temp_date = instance.estimated_end_date - datetimelib.timedelta(
                                days=instance.certificatio_type.estimated_days)

                instance.delivery_date = temp_date


            elif schould_generate_delivery_date == "False":
                print("Delivery date generetion: False")
                pass



            print("---------------------------------------")
            print("Add - Certification Item - for Schedule")
            print("---------------------------------------")
            aaa = "{:20} - {:12}"
            print(aaa.format("Generate start date", schould_generate_delivery_date))
            print(aaa.format("Generate end date", schould_generate_end_date))
            print("start date")
            print(instance.delivery_date)
            print("end date")
            print(instance.estimated_end_date)
            print(aaa.format("estimated_days", instance.certificatio_type.estimated_days))
            print("---------------------------------------")


            instance.save()
            return HttpResponseRedirect(reverse('schedule:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_ScheduleItemCertification_View(UpdateView):
    model = ScheduleItem_Certification
    form_class = Create_ScheduleItemCertification_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Certification Item"}
    info_text = {"info_text": "Delete this Certification Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Update_ScheduleItemCertification_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Delete_ScheduleItemCertification_View(DeleteView):
    model = ScheduleItem_Certification
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Certification Item"}
    info_text = {"info_text": "Delete this Certification Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_ScheduleItemCertification_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Create_MeasurementType_View(View):
    form_class = Create_MeasurementType_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Create Measurement Type"}
    # title = "Create Schedule"
    def get(self, request, *args, **kwargs):

        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.created_user = request.user
            # instance.save()
            form.save()
            return HttpResponseRedirect(reverse('schedule:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_MeasurementType_View(UpdateView):
    model = Measurement_Type
    form_class = Create_MeasurementType_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Measurement Type"}
    info_text = {"info_text": "Delete this Measurement Type - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Update_MeasurementType_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Delete_MeasurementType_View(DeleteView):
    model = Measurement_Type
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Measurement Type"}
    info_text = {"info_text": "Delete this Measurement Type - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_MeasurementType_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Create_ScheduleItemMeasurement_View(View):
    # Form Klasse abspeichern
    form_class = Create_ScheduleItemMeasurement_Form
    # Template Name abspeichern
    template_name = 'schedule/schedule_createForm.html'
    # Panel Titel erstellen
    panel_titel = {"panel_titel" : "Create Schedule Item Measurement"}

    # GET Methode
    def get(self, request, *args, **kwargs):

        # Felder initialisieren
        #   - Ersteller
        #   - Erstellungs Datum
        initial = {
            "created_user" : request.user,
            "creation_date" : datetime.now(),
        }

        # Form erstellen mit den initialisierten Feldern
        form = self.form_class(initial=initial)
        # Den Usernamen auslesen --> wird gleich gebraucht um die schedules
        #  des Users zu laden
        username_request = self.request.user.username
        # jetzt nur die schedules des users in das form field "schedule" laden
        form.fields["schedule"].queryset = Schedule.objects.filter(
            created_user__username=username_request)
        # Context abspeichern
        context = {'form': form}
        # Panel Titel noch vergeben
        context.update(self.panel_titel)
        # DEBUG: Form informationen ausgeben
        print("")
        # HTML Document rendern
        return render(request, self.template_name, context)

    # POST Methode
    def post(self, request, *args, **kwargs):
        """
            die beiden checkbox button
                - True
                - False
            sind in der variable
                -- request.POST["eut_date_calculation"] --
            gespeichert
        """

        # Erstmal die empfangene Form speichern
        form = self.form_class(request.POST)

        # jetzt den Wert der "end_date_calculation" radiobuttons
        # zwischenspeichern
        #  anhand dieses wertes wird das "end_date" selbst berechnet
        #  oder der wert des DateTimeInputs wird uebernommen
        #      - false = wert uebernehmen
        #      - true  = wert anhand des measurement types berechnen
        schould_generate_end_date = request.POST["end_date_calculation"]

        # checken ob die Form ok ist
        if form.is_valid():
            instance = form.save(commit=False)

            instance.created_user = request.user

            # Wenn das estimated_end_date berechnet werden soll
            # dann ist die Variable True
            if schould_generate_end_date == "True":
                # ersteinmal ein temporaeres datum erstellen
                # anhand des delivery_date
                # (plus) die anzahl an tagen aus dem measurement_type
                # mithilfe der Python Standard Klasse (timedelta)
                temp_date = instance.delivery_date + datetimelib.timedelta(
                                days=instance.measurement_type.estimated_days)

                # jetzt noch das temporaere datum in die estimated_end_date
                # variable des (objects) instance schreiben
                instance.estimated_end_date = temp_date
            elif schould_generate_end_date == "Flase":
                pass

            # jetzt das (object) instance speichern
            instance.save()

            # jetzt noch eine HTTP Redirect auf die index Seite
            return HttpResponseRedirect(reverse('schedule:index'))

        # wenn nicht valide dann einen render
        # mit der neuen form
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_ScheduleItemMeasurement_View(UpdateView):
    model = ScheduleItem_Measurement
    form_class = Create_ScheduleItemMeasurement_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Measurement Item"}
    info_text = {"info_text": "Delete this Measurement Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Update_ScheduleItemMeasurement_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Delete_ScheduleItemMeasurement_View(DeleteView):
    model = ScheduleItem_Measurement
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Measurement Item"}
    info_text = {"info_text": "Delete this Measurement Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_ScheduleItemMeasurement_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class Create_ScheduleItemMaterial_View(View):
    form_class = Create_ScheduleItemMaterial_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Create Schedule Item Material"}
    # title = "Create Schedule"
    def get(self, request, *args, **kwargs):

        initial = {
            "created_user" : request.user,
            "creation_date" : datetime.now(),
        }

        form = self.form_class(initial=initial)
        username_request = self.request.user.username
        form.fields["schedule"].queryset = Schedule.objects.filter(created_user__username=username_request)
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user
            instance.save()
            form.save()
            return HttpResponseRedirect(reverse('schedule:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_ScheduleItemMaterial_View(UpdateView):
    model = ScheduleItem_Material
    form_class = Create_ScheduleItemMaterial_Form
    template_name = 'schedule/schedule_createForm.html'
    panel_titel = {"panel_titel" : "Update Material Item"}
    info_text = {"info_text": "Delete this Material Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Update_ScheduleItemMaterial_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)

        # form aus dem context holen
        form = context["form"]
        # username aus dem request holen
        username_request = self.request.user.username
        print("-------------")
        print(username_request)
        print("-------------")
        # neues queryset in das form feld laden
        form.fields["schedule"].queryset = Schedule.objects.filter(created_user__username=username_request)
        # und wieder die form als form im context abspeichern
        context["form"] = form

        return context

@method_decorator(login_required, name='dispatch')
class Delete_ScheduleItemMaterial_View(DeleteView):
    model = ScheduleItem_Material
    template_name = 'schedule/schedule_createForm.html'
    success_url = reverse_lazy("schedule:index")
    panel_titel = {"panel_titel" : "Delete Material Item"}
    info_text = {"info_text": "Delete this Material Item - please push 'OK' to submit the changes"}

    def get_context_data(self, **kwargs):
        context = super(Delete_ScheduleItemMaterial_View, self).get_context_data(**kwargs)
        context.update(self.panel_titel)
        context.update(self.info_text)
        return context

@method_decorator(login_required, name='dispatch')
class View_Schedule_objects(View):
    template_name = 'schedule/schedule_viewAllObjects.html'
    form_title = {"form_title" : "Create Schedule Item Material"}

    def get(self, request, *args, **kwargs):

        context = {}
        context.update(self.form_title)


        temp = Schedule.objects.all()
        context["list_schedule"] = reversed(temp)

        temp = ScheduleItem_Material.objects.all()
        context["list_item_material"] = list(reversed(temp))

        temp = Measurement_Type.objects.all()
        context["list_type_measurement"] = list(reversed(temp))

        temp = ScheduleItem_Measurement.objects.all()
        context["list_item_measurement"] = list(reversed(temp))

        temp = Certification_Type.objects.all()
        context["list_type_certification"] = list(reversed(temp))

        temp = ScheduleItem_Certification.objects.all()
        context["list_item_certification"] = list(reversed(temp))

        for i in context:
            print(i + str(context[i]))


        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class View_a_schedule(View):
    template_name = 'schedule/schedule_viewASchedule.html'
    form_title = {"form_title" : "Create Schedule Item Material"}

    def get(self, request, *args, **kwargs):

        # DEBUG START
        print("---------------")
        print("DEBUG - request")
        print("---------------")
        print(request)
        print("---------------")
        print("DEBUG - args")
        print("---------------")
        print(args)
        print("---------------")
        print("DEBUG - kwargs")
        print("---------------")
        print(kwargs)
        print("---------------")
        # DEBUG ENDE



        context = {}

        schedule_id = kwargs["schedule_id"]
        print("schedule id: " + str(schedule_id))

        schedule_object = Schedule.objects.get(pk=schedule_id)
        print(schedule_object)
        context["schedule_object"] = schedule_object

        schedule_material_list = ScheduleItem_Material.objects.filter(schedule__id=schedule_id)
        print(schedule_material_list)
        context["schedule_material_list"] = schedule_material_list

        schedule_measurement_list = ScheduleItem_Measurement.objects.filter(schedule__id=schedule_id)
        print(schedule_measurement_list)
        #context["schedule_measurement_list"] = schedule_measurement_list

        from operator import itemgetter, attrgetter, methodcaller
        context["schedule_measurement_list"] = sorted(
            schedule_measurement_list, key=attrgetter('delivery_date'))

        schedule_certification_list = ScheduleItem_Certification.objects.filter(schedule__id=schedule_id)
        print(schedule_certification_list)
        context["schedule_certification_list"] = schedule_certification_list


        # generate the schedule item list
        item_counter = 0
        schedule_item_list = []

        system_object = schedule_object.system
        msdbconnection_list = MSDBConnention.objects.filter(system=system_object)

        print(msdbconnection_list)

        for item in msdbconnection_list:
            item_counter = item_counter + 1
            a = {}
            a['id'] = item_counter
            a['group'] = 0
            a['content'] = item.milestone.name
            a['start'] = str(   str(item.milestoneFinish_date.year) + '-' +
                                str(item.milestoneFinish_date.month) + '-' +
                                str(item.milestoneFinish_date.day)
                                )
            schedule_item_list.append(a)


        for item in schedule_measurement_list:
            item_counter = item_counter + 1
            a = {}
            a['id'] = item_counter
            a['group'] = 1
            a['content'] = item.name
            a['start'] = str(   str(item.delivery_date.year) + '-' +
                                str(item.delivery_date.month) + '-' +
                                str(item.delivery_date.day)
                                )
            a['end'] = str(     str(item.estimated_end_date.year) + '-' +
                                str(item.estimated_end_date.month) + '-' +
                                str(item.estimated_end_date.day)
                                )

            schedule_item_list.append(a)





        for item in schedule_certification_list:
            item_counter = item_counter + 1
            a = {}
            a['id'] = item_counter
            a['group'] = 2
            a['content'] = item.name
            a['start'] = str(   str(item.delivery_date.year) + '-' +
                                str(item.delivery_date.month) + '-' +
                                str(item.delivery_date.day)
                                )
            a['end'] = str(     str(item.estimated_end_date.year) + '-' +
                                str(item.estimated_end_date.month) + '-' +
                                str(item.estimated_end_date.day)
                                )

            schedule_item_list.append(a)


        for item in schedule_material_list:
            item_counter = item_counter + 1
            a = {}
            a['id'] = item_counter
            a['group'] = 3
            a['content'] = item.name
            a['start'] = str(   str(item.delivery_date.year) + '-' +
                                str(item.delivery_date.month) + '-' +
                                str(item.delivery_date.day)
                                )
            schedule_item_list.append(a)



        group_item_list = []

        group_item_list.append({"id":0, "content":"MS"})
        group_item_list.append({"id":1, "content":"Measurements"})
        group_item_list.append({"id":2, "content":"Certifications"})
        group_item_list.append({"id":3, "content":"Materials"})



        # nochmal die listen checken mit print
        print("\n Schedule Item List:\n")
        for i in schedule_item_list:
            print(i)

        print("\n Group Item List:\n")
        for i in group_item_list:
            print(i)

        context["schedule_items"] = json.dumps(schedule_item_list)
        context["groups_items"] = json.dumps(group_item_list)
        return render(request, self.template_name, context)
