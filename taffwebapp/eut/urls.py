from django.conf.urls import url
from . import views

app_name = 'eut'

urlpatterns = [
    # incomming tag is /eut/

    url(r'^eut/$',                      views.Eut_MainView.as_view() , name='index'),
    url(r'^eutlist/$',                  views.Eut_list_view.as_view() , name='eut_list'),
    url(r'^eut/(?P<pk>[0-9]+)/$',       views.Eut_detail_view.as_view(), name='eut_detail'),
    url(r'^eut/add/$',                  views.Eut_Create_view.as_view() , name='eut_create'),



    # Spezial Link
    # Loescht eine Componente aus einem EUT anhand des pk der eut component connection
    url(r'^deleteEutToComponentConnection/(?P<pk>[0-9]+)/$',       views.DeleteComponentEutConnection.as_view(), name='eut_delete_component_to_eut_connection'),

]
