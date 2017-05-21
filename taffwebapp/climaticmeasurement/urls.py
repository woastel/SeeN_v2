from django.conf.urls import url
from . import views

app_name = 'climaticmeasurement'

urlpatterns = [
    # /euts/
    url(r'^cm/$', views.MainView.as_view() , name='index'),

    # Create Climaticmeasurements
    ## by MCPS-Statistik File
    ## or by csv File
    url(r'^cm/create/cmbymcps/$', views.CreateCM_byMCPS.as_view(), name='create_cm_bymcps'),

    # Create Sensor Type List
    url(r'^cm/create/sensortypeList/$', views.CreateCM_byMCPS.as_view, name='create_sensortypeList'),

    url(r'^cm/showAll/$', views.show_list_of_cm.as_view(), name='show_all_climaticmeasurements'),

    url(r'^cm/show/(?P<measurement_id>[0-9]+)/$', views.show_CM.as_view(), name='show_climaticmeasurement'),
]
