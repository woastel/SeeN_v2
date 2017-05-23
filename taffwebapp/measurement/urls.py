from django.conf.urls import url
from . import views

from measurement.views import (
    view_measurement,
    view_measurement_climatic,
    view_measurement_emi)

app_name = 'measurement'

urlpatterns = [
    # Measurement (general) Views
    url(r'^measurement/$',          view_measurement.IndexView.as_view() ,                          name='m_index'),

    # Measurement Climatic (cm) Views
    url(r'^measurement_climatic/$',                 view_measurement_climatic.IndexView.as_view() ,                         name='mc_index'),
    url(r'^measurement_climatic/create/cmbymcps/$', view_measurement_climatic.CreateCM_byMCPS.as_view(),                    name='mc_create_bymcps'),
    url(r'^measurement_climatic/listview/$',        view_measurement_climatic.ListOfClimaticMeasurements_View.as_view() ,   name='mc_list'),
    url(r'^measurement_climatic/(?P<pk>[0-9]+)/$',  view_measurement_climatic.DetailClimaticMeasurement_View.as_view(),     name='mc_detail_view'),

    # Add Climatic Measurement Spezific Attributes
    url(r'^measurement_climatic/add/ambientTemp/$', view_measurement_climatic.Create_AmbientTemperature.as_view() ,      name='mc_add_AmbientTemperature'),
    url(r'^measurement_climatic/add/testLoad/$', view_measurement_climatic.Create_TestLoad.as_view() ,      name='mc_add_TestLoad'),
    url(r'^measurement_climatic/add/SensorTypeList/$', view_measurement_climatic.Create_SensorTypeList.as_view() ,      name='mc_add_SensorTypeList'),

    # Measurement EMI (memi) Views
    url(r'^measurement_emi/$',      view_measurement_emi.IndexView.as_view() ,                      name='memi_index'),


]
