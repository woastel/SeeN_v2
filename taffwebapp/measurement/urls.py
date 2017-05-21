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
    url(r'^measurement_climatic/$', view_measurement_climatic.IndexView.as_view() ,                          name='mc_index'),
    url(r'^measurement_climatic/create/cmbymcps/$', view_measurement_climatic.CreateCM_byMCPS.as_view(),     name='mc_create_bymcps'),


    # Measurement EMI (memi) Views
    url(r'^measurement_emi/$',      view_measurement_emi.IndexView.as_view() ,                      name='memi_index'),


]
