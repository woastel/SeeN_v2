from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from . import forms
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from .models import (
        Component,
        Chassis,
        ChassisAddOn,
        Motherboard,
        Cpu,
        Memory,
        PSU,
        HDD,
        HeatSink,
        Fan,
        Cable,
        Pcba,
        Pcie_Ctrl)


#
# Main View
#-------------------------
@method_decorator(login_required, name='dispatch')
class MainView(View):
    templateName = 'components/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        usernameRequest = self.request.user.username

        # Anzahl der Componenten holen
        component_anzahl = len(Component.objects.all())
        context["component_anzahl"] = component_anzahl

        # get the last updated component object
        try:
            component_last_updated = Component.objects.all().order_by('-date_update')[0]
            context["component_last_updated"] = component_last_updated
        except:
            print("Error: Keine Componenten vorhanden")

        # get the last component object - ( is the object with the max id)
        try:
            component_last_added = Component.objects.all().order_by("-component_id")[0]
            context["component_last_added"] = component_last_added
        except:
            print("Error: Keine Componenten vorhanden")


        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class List_Component_View(View):
    templateName = 'components/component_list_view.html'
    panel_titel = "Component List View"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}

        context["component_list"] = Component.objects.all()
        nearby_places = Component.objects.filter(character_thermal_avalible=True).select_subclasses()

        print("\n\n----------------------")

        for i in nearby_places:
            print(str(i) + " Temp: " + str(i.temperature_max))

        print("----------------------\n\n")

        print(context["component_list"])
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Detail_Component_View(View):
    templateName = 'components/component_detail_view.html'
    panel_titel = "Component Detail View"

    def get(self, request, *args, **kwargs):
        # context dictonary - render context
        print(kwargs)
        context = {}
        context['alert_success_avalible'] = False
        context['alert_danger_avalible'] = False
        # component id
        var_component_id = kwargs["pk"]
        # get the component - but select the subclasses
        var_component = Component.objects.filter(component_id=var_component_id).select_subclasses()

        # put the component into the dictonary
        # check if the querysert has a object
        if len(var_component) != 0:
            context['component'] = var_component[0]
            context['alert_success_avalible'] = True
            context['alert_success'] = str(
                'Pass - Component with id({}) is avalible.'.format(var_component_id))
        else:
            context['alert_danger_avalible'] = True
            context['alert_danger'] = str(
                'Error - Component with id({}) isnt avalible.'.format(var_component_id))


        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)




#
# Create Types + Vendor
#-------------------------
#@method_decorator(login_required, name='dispatch')
#class Create_Component_Type_View(View):
#    form_class = forms.Form_Component_Type
#    templateName = 'components/component_create.html'
#    panel_titel = "Create a new Component Type"
#
#    def get(self, request, *args, **kwargs):
#        # context that schould be render
#        context = {}
#        # inital date for the form
#        initial = {}
#        # generate the form with the initals
#        form = self.form_class(initial=initial)
#        # add the form to the context
#        context.update({'form': form})
#        # add the panel titel to the context
#        context.update({'panel_titel': self.panel_titel})
#        # now return the render object with template name and context
#        return render(request, self.templateName, context)
#
#    def post(self, request, *args, **kwargs):
#        # first save the form with the request Post arguments
#        form = self.form_class(request.POST)
#        print(request.POST)
#
#        # check if form is valid
#        if form.is_valid():
#            # then get the instance from the form without commit
#            instance = form.save(commit=False)
#            # change some attributes from the instance
#            ## -- this instance have no creator instance.created_user = request.user
#            # save the instance
#            instance.save()
#            # return a http redirect
#            return HttpResponseRedirect(reverse('components:index'))
#
#        # if form is not valid - return the form object like the
#        #  get method
#        context = {'form': form}
#        context.update(self.panel_titel)
#        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Create_Vendor_View(View):
    form_class = forms.Form_Vendor
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Vendor"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            ## -- this instance have no creator instance.created_user = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


# Chassis Views
@method_decorator(login_required, name='dispatch')
class Create_Chassis_View(View):
    form_class = forms.Form_Chassis
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Chassis"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Chassis_View(generic.UpdateView):
    form_class = forms.Form_Chassis
    model = Chassis
    template_name = "components/component_create.html"
    #success_url = reverse_lazy('components:index'  kwargs={'pk': })

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Chassis_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    #def get_success_url(self):
    #    return reverse('components:component_detail', kwargs={'pk': self.object.component_id})

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Chassis_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Chassis_View(generic.DeleteView):
    model = Chassis
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")



# Chassis Add On Views
@method_decorator(login_required, name='dispatch')
class Create_ChassisAddOn_View(View):
    form_class = forms.Form_ChassisAddOn
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Chassis Add On"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_ChassisAddOn_View(generic.UpdateView):
    form_class = forms.Form_ChassisAddOn
    model = ChassisAddOn
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_ChassisAddOn_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_ChassisAddOn_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_ChassisAddOn_View(generic.DeleteView):
    model = ChassisAddOn
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")








# Motherboard Views
@method_decorator(login_required, name='dispatch')
class Create_Motherboard_View(View):
    form_class = forms.Form_Motherboard
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Motherboard"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Motherboard_View(generic.UpdateView):
    form_class = forms.Form_Motherboard
    model = Motherboard
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Motherboard_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Motherboard_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Motherboard_View(generic.DeleteView):
    model = Motherboard
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")





# CPU Views
@method_decorator(login_required, name='dispatch')
class Create_CPU_View(View):
    form_class = forms.Form_Cpu
    templateName = 'components/component_create.html'
    panel_titel = "Create a new CPU"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_CPU_View(generic.UpdateView):
    form_class = forms.Form_Cpu
    model = Cpu
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_CPU_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_CPU_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_CPU_View(generic.DeleteView):
    model = Cpu
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")





# Memory Views
@method_decorator(login_required, name='dispatch')
class Create_Memory_View(View):
    form_class = forms.Form_Memory
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Memory"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Memory_View(generic.UpdateView):
    form_class = forms.Form_Memory
    model = Memory
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Memory_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Memory_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Memory_View(generic.DeleteView):
    model = Memory
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")



# PSU Views
@method_decorator(login_required, name='dispatch')
class Create_PSU_View(View):
    form_class = forms.Form_PSU
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PSU"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_PSU_View(generic.UpdateView):
    form_class = forms.Form_PSU
    model = PSU
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_PSU_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_PSU_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_PSU_View(generic.DeleteView):
    model = PSU
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")




# HDD Views
@method_decorator(login_required, name='dispatch')
class Create_HDD_View(View):
    form_class = forms.Form_HDD
    templateName = 'components/component_create.html'
    panel_titel = "Create a new HDD"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_HDD_View(generic.UpdateView):
    form_class = forms.Form_HDD
    model = HDD
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_HDD_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_HDD_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_HDD_View(generic.DeleteView):
    model = HDD
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")




# Heat Sink Views
@method_decorator(login_required, name='dispatch')
class Create_HeatSink_View(View):
    form_class = forms.Form_HeatSink
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Heatsink"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_HeatSink_View(generic.UpdateView):
    form_class = forms.Form_HeatSink
    model = HeatSink
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_HeatSink_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_HeatSink_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_HeatSink_View(generic.DeleteView):
    model = HeatSink
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")



# Fan Views
@method_decorator(login_required, name='dispatch')
class Create_Fan_View(View):
    form_class = forms.Form_Fan
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Fan"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Fan_View(generic.UpdateView):
    form_class = forms.Form_Fan
    model = Fan
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Fan_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Fan_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Fan_View(generic.DeleteView):
    model = Fan
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")


# Cable Views
@method_decorator(login_required, name='dispatch')
class Create_Cable_View(View):
    form_class = forms.Form_Cable
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Cable"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Cable_View(generic.UpdateView):
    form_class = forms.Form_Cable
    model = Cable
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Cable_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Cable_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Cable_View(generic.DeleteView):
    model = Cable
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")



# PCBA Views
@method_decorator(login_required, name='dispatch')
class Create_Pcba_View(View):
    form_class = forms.Form_Pcba
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PCBA"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_Pcba_View(generic.UpdateView):
    form_class = forms.Form_Pcba
    model = Pcba
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_Pcba_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_Pcba_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_Pcba_View(generic.DeleteView):
    model = Pcba
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")


# PCIe Ctrl Views
@method_decorator(login_required, name='dispatch')
class Create_PcieCtrl_View(View):
    form_class = forms.Form_Pcie_Ctrl
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PCIe Ctrl."

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Update_PcieCtrl_View(generic.UpdateView):
    form_class = forms.Form_Pcie_Ctrl
    model = Pcie_Ctrl
    template_name = "components/component_create.html"

    def get_object(self):
        # it doesn't matter how many times get_object is called per request
        # it should not do more than one request
        if not hasattr(self, '_object'):
            self._object = super(Update_PcieCtrl_View, self).get_object()

        # now update the user and date
        self._object.user_updater = self.request.user
        self._object.date_update = datetime.now()

        return self._object

    def form_valid(self, form):
        form.save()
        context = {}
        context['component'] = self.object
        context['alert_success_avalible'] = True
        context['alert_success'] = str(
            'Component Update is PASS'.format(self.object.component_id))

        return render(self.request, 'components/component_detail_view.html', context)

    def get_context_data(self, **kwargs):
        # erstmal selber aufrufen um die context daten zu bekommen
        context = super(Update_PcieCtrl_View, self).get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
class Delete_PcieCtrl_View(generic.DeleteView):
    model = Pcie_Ctrl
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy("components:index")
