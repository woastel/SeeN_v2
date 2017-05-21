from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic, View
from .forms import UploadFileForm
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .readMcpsFile import readMcpsStatisticFile
from .cm_table_generator import cm_table_list_generator
from .models import Climaticmeasure, MeasureValues, SensorMax, SensorName, SensorValue



@method_decorator(login_required, name='dispatch')
class MainView(View):
    template_name = 'climaticmeasurement/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class show_list_of_cm(View):
    template_name = "climaticmeasurement\list_of_measurements.html"

    def get(self, request, *args, **kwargs):

        context = {}

        measurement_list = Climaticmeasure.objects.all()
        context["measurement_list"] = measurement_list

        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class show_CM(View):
    template_name = "climaticmeasurement\climaticmeasure_table.html"

    def get(self, request, *args, **kwargs):

        measurementid = kwargs["measurement_id"]
        context = {}

        Cmeasurement_object = Climaticmeasure.objects.get(pk=measurementid)
        context["measurement_object"] = Cmeasurement_object
        obj = cm_table_list_generator(Cmeasurement_object)
        context["obj"] = obj
        for i in obj.table_rows:
            print(i.name)


        return render(request, self.template_name, context)



@method_decorator(login_required, name='dispatch')
class CreateCM_byMCPS(View):
    form_class = UploadFileForm
    template_name = 'climaticmeasurement/upload-MCPS-file.html'
    panel_titel = { "panel_titel": "Create Climatic-Measurement by MCPS File"}
    def get(self, request, *args, **kwargs):

        initial =  {
            "creation_date": datetime.now(),
            "creator": request.user,

        }

        form = self.form_class(initial=initial)

        context = {'form': form}
        context.update(self.panel_titel)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        print("CHEKC BASTI")

        if form.is_valid():
            print("CHEKC BASTI")
            instance = form.save(commit=False)
            instance.created_user = request.user

            mcpsfile_obj = readMcpsStatisticFile(request.FILES["file"], request.user.username)


            maxvalue_dict = mcpsfile_obj.sensorMax
            sensormax_temp = create_sensorMax_model(maxvalue_dict)
            sensormax_temp.save()


            namee_dict = mcpsfile_obj.sensorName
            sensorname_temp = create_sensorName_model(namee_dict)
            sensorname_temp.save()


            valuee_dict = mcpsfile_obj.sensorValue
            sensorvalue_temp = create_sensorValue_model(valuee_dict)
            sensorvalue_temp.save()


            measurement_values = MeasureValues()
            measurement_values.name = mcpsfile_obj.mcpsInfoLine
            measurement_values.info = mcpsfile_obj.mcpsInfoLine
            measurement_values.sensorMax_id_fk = sensormax_temp
            measurement_values.sensorName_id_fk = sensorname_temp
            measurement_values.sensorValue_id_fk = sensorvalue_temp
            measurement_values.save()


            instance.measureValues_id_fk = measurement_values



            instance.save()
            print(instance)


            return HttpResponseRedirect(reverse('climaticmeasurement:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

def create_sensorMax_model(max_dict):
    sensormax_temp = SensorMax()
    sensormax_temp.name_list = "max"
    sensormax_temp.max1  = max_dict["max1"]
    sensormax_temp.max2  = max_dict["max2"]
    sensormax_temp.max3  = max_dict["max3"]
    sensormax_temp.max4  = max_dict["max4"]
    sensormax_temp.max5  = max_dict["max5"]
    sensormax_temp.max6  = max_dict["max6"]
    sensormax_temp.max7  = max_dict["max7"]
    sensormax_temp.max8  = max_dict["max8"]
    sensormax_temp.max9  = max_dict["max9"]
    sensormax_temp.max10 = max_dict["max10"]
    sensormax_temp.max11 = max_dict["max11"]
    sensormax_temp.max12 = max_dict["max12"]
    sensormax_temp.max13 = max_dict["max13"]
    sensormax_temp.max14 = max_dict["max14"]
    sensormax_temp.max15 = max_dict["max15"]
    sensormax_temp.max16 = max_dict["max16"]
    sensormax_temp.max17 = max_dict["max17"]
    sensormax_temp.max18 = max_dict["max18"]
    sensormax_temp.max19 = max_dict["max19"]
    sensormax_temp.max20 = max_dict["max20"]
    sensormax_temp.max21 = max_dict["max21"]
    sensormax_temp.max22 = max_dict["max22"]
    sensormax_temp.max23 = max_dict["max23"]
    sensormax_temp.max24 = max_dict["max24"]
    sensormax_temp.max25 = max_dict["max25"]
    sensormax_temp.max26 = max_dict["max26"]
    sensormax_temp.max27 = max_dict["max27"]
    sensormax_temp.max28 = max_dict["max28"]
    sensormax_temp.max29 = max_dict["max29"]
    sensormax_temp.max30 = max_dict["max30"]
    sensormax_temp.max31 = max_dict["max31"]
    sensormax_temp.max32 = max_dict["max32"]
    sensormax_temp.max33 = max_dict["max33"]
    sensormax_temp.max34 = max_dict["max34"]
    sensormax_temp.max35 = max_dict["max35"]
    sensormax_temp.max36 = max_dict["max36"]
    sensormax_temp.max37 = max_dict["max37"]
    sensormax_temp.max38 = max_dict["max38"]
    sensormax_temp.max39 = max_dict["max39"]
    sensormax_temp.max40 = max_dict["max40"]
    sensormax_temp.max41 = max_dict["max41"]
    sensormax_temp.max42 = max_dict["max42"]
    sensormax_temp.max43 = max_dict["max43"]
    sensormax_temp.max44 = max_dict["max44"]
    sensormax_temp.max45 = max_dict["max45"]
    sensormax_temp.max46 = max_dict["max46"]
    sensormax_temp.max47 = max_dict["max47"]
    sensormax_temp.max48 = max_dict["max48"]
    sensormax_temp.max49 = max_dict["max49"]
    sensormax_temp.max50 = max_dict["max50"]
    sensormax_temp.max51 = max_dict["max51"]
    sensormax_temp.max52 = max_dict["max52"]
    sensormax_temp.max53 = max_dict["max53"]
    sensormax_temp.max54 = max_dict["max54"]
    sensormax_temp.max55 = max_dict["max55"]
    sensormax_temp.max56 = max_dict["max56"]
    sensormax_temp.max57 = max_dict["max57"]
    sensormax_temp.max58 = max_dict["max58"]
    sensormax_temp.max59 = max_dict["max59"]
    sensormax_temp.max60 = max_dict["max60"]

    return sensormax_temp

def create_sensorName_model(name_dict):
    sensornamemodel_temp = SensorName()
    sensornamemodel_temp.name_list = "name"
    sensornamemodel_temp.name1  = name_dict["name1"]
    sensornamemodel_temp.name2  = name_dict["name2"]
    sensornamemodel_temp.name3  = name_dict["name3"]
    sensornamemodel_temp.name4  = name_dict["name4"]
    sensornamemodel_temp.name5  = name_dict["name5"]
    sensornamemodel_temp.name6  = name_dict["name6"]
    sensornamemodel_temp.name7  = name_dict["name7"]
    sensornamemodel_temp.name8  = name_dict["name8"]
    sensornamemodel_temp.name9  = name_dict["name9"]
    sensornamemodel_temp.name10 = name_dict["name10"]
    sensornamemodel_temp.name11 = name_dict["name11"]
    sensornamemodel_temp.name12 = name_dict["name12"]
    sensornamemodel_temp.name13 = name_dict["name13"]
    sensornamemodel_temp.name14 = name_dict["name14"]
    sensornamemodel_temp.name15 = name_dict["name15"]
    sensornamemodel_temp.name16 = name_dict["name16"]
    sensornamemodel_temp.name17 = name_dict["name17"]
    sensornamemodel_temp.name18 = name_dict["name18"]
    sensornamemodel_temp.name19 = name_dict["name19"]
    sensornamemodel_temp.name20 = name_dict["name20"]
    sensornamemodel_temp.name21 = name_dict["name21"]
    sensornamemodel_temp.name22 = name_dict["name22"]
    sensornamemodel_temp.name23 = name_dict["name23"]
    sensornamemodel_temp.name24 = name_dict["name24"]
    sensornamemodel_temp.name25 = name_dict["name25"]
    sensornamemodel_temp.name26 = name_dict["name26"]
    sensornamemodel_temp.name27 = name_dict["name27"]
    sensornamemodel_temp.name28 = name_dict["name28"]
    sensornamemodel_temp.name29 = name_dict["name29"]
    sensornamemodel_temp.name30 = name_dict["name30"]
    sensornamemodel_temp.name31 = name_dict["name31"]
    sensornamemodel_temp.name32 = name_dict["name32"]
    sensornamemodel_temp.name33 = name_dict["name33"]
    sensornamemodel_temp.name34 = name_dict["name34"]
    sensornamemodel_temp.name35 = name_dict["name35"]
    sensornamemodel_temp.name36 = name_dict["name36"]
    sensornamemodel_temp.name37 = name_dict["name37"]
    sensornamemodel_temp.name38 = name_dict["name38"]
    sensornamemodel_temp.name39 = name_dict["name39"]
    sensornamemodel_temp.name40 = name_dict["name40"]
    sensornamemodel_temp.name41 = name_dict["name41"]
    sensornamemodel_temp.name42 = name_dict["name42"]
    sensornamemodel_temp.name43 = name_dict["name43"]
    sensornamemodel_temp.name44 = name_dict["name44"]
    sensornamemodel_temp.name45 = name_dict["name45"]
    sensornamemodel_temp.name46 = name_dict["name46"]
    sensornamemodel_temp.name47 = name_dict["name47"]
    sensornamemodel_temp.name48 = name_dict["name48"]
    sensornamemodel_temp.name49 = name_dict["name49"]
    sensornamemodel_temp.name50 = name_dict["name50"]
    sensornamemodel_temp.name51 = name_dict["name51"]
    sensornamemodel_temp.name52 = name_dict["name52"]
    sensornamemodel_temp.name53 = name_dict["name53"]
    sensornamemodel_temp.name54 = name_dict["name54"]
    sensornamemodel_temp.name55 = name_dict["name55"]
    sensornamemodel_temp.name56 = name_dict["name56"]
    sensornamemodel_temp.name57 = name_dict["name57"]
    sensornamemodel_temp.name58 = name_dict["name58"]
    sensornamemodel_temp.name59 = name_dict["name59"]
    sensornamemodel_temp.name60 = name_dict["name60"]

    return sensornamemodel_temp

def create_sensorValue_model(value_dict):
    sensornamemodel_temp = SensorValue()
    sensornamemodel_temp.name_list = "value"
    sensornamemodel_temp.value1  = value_dict["value1"]
    sensornamemodel_temp.value2  = value_dict["value2"]
    sensornamemodel_temp.value3  = value_dict["value3"]
    sensornamemodel_temp.value4  = value_dict["value4"]
    sensornamemodel_temp.value5  = value_dict["value5"]
    sensornamemodel_temp.value6  = value_dict["value6"]
    sensornamemodel_temp.value7  = value_dict["value7"]
    sensornamemodel_temp.value8  = value_dict["value8"]
    sensornamemodel_temp.value9  = value_dict["value9"]
    sensornamemodel_temp.value10 = value_dict["value10"]
    sensornamemodel_temp.value11 = value_dict["value11"]
    sensornamemodel_temp.value12 = value_dict["value12"]
    sensornamemodel_temp.value13 = value_dict["value13"]
    sensornamemodel_temp.value14 = value_dict["value14"]
    sensornamemodel_temp.value15 = value_dict["value15"]
    sensornamemodel_temp.value16 = value_dict["value16"]
    sensornamemodel_temp.value17 = value_dict["value17"]
    sensornamemodel_temp.value18 = value_dict["value18"]
    sensornamemodel_temp.value19 = value_dict["value19"]
    sensornamemodel_temp.value20 = value_dict["value20"]
    sensornamemodel_temp.value21 = value_dict["value21"]
    sensornamemodel_temp.value22 = value_dict["value22"]
    sensornamemodel_temp.value23 = value_dict["value23"]
    sensornamemodel_temp.value24 = value_dict["value24"]
    sensornamemodel_temp.value25 = value_dict["value25"]
    sensornamemodel_temp.value26 = value_dict["value26"]
    sensornamemodel_temp.value27 = value_dict["value27"]
    sensornamemodel_temp.value28 = value_dict["value28"]
    sensornamemodel_temp.value29 = value_dict["value29"]
    sensornamemodel_temp.value30 = value_dict["value30"]
    sensornamemodel_temp.value31 = value_dict["value31"]
    sensornamemodel_temp.value32 = value_dict["value32"]
    sensornamemodel_temp.value33 = value_dict["value33"]
    sensornamemodel_temp.value34 = value_dict["value34"]
    sensornamemodel_temp.value35 = value_dict["value35"]
    sensornamemodel_temp.value36 = value_dict["value36"]
    sensornamemodel_temp.value37 = value_dict["value37"]
    sensornamemodel_temp.value38 = value_dict["value38"]
    sensornamemodel_temp.value39 = value_dict["value39"]
    sensornamemodel_temp.value40 = value_dict["value40"]
    sensornamemodel_temp.value41 = value_dict["value41"]
    sensornamemodel_temp.value42 = value_dict["value42"]
    sensornamemodel_temp.value43 = value_dict["value43"]
    sensornamemodel_temp.value44 = value_dict["value44"]
    sensornamemodel_temp.value45 = value_dict["value45"]
    sensornamemodel_temp.value46 = value_dict["value46"]
    sensornamemodel_temp.value47 = value_dict["value47"]
    sensornamemodel_temp.value48 = value_dict["value48"]
    sensornamemodel_temp.value49 = value_dict["value49"]
    sensornamemodel_temp.value50 = value_dict["value50"]
    sensornamemodel_temp.value51 = value_dict["value51"]
    sensornamemodel_temp.value52 = value_dict["value52"]
    sensornamemodel_temp.value53 = value_dict["value53"]
    sensornamemodel_temp.value54 = value_dict["value54"]
    sensornamemodel_temp.value55 = value_dict["value55"]
    sensornamemodel_temp.value56 = value_dict["value56"]
    sensornamemodel_temp.value57 = value_dict["value57"]
    sensornamemodel_temp.value58 = value_dict["value58"]
    sensornamemodel_temp.value59 = value_dict["value59"]
    sensornamemodel_temp.value60 = value_dict["value60"]

    return sensornamemodel_temp
