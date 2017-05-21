from django.conf.urls import url
from . import views

app_name = 'overview'

urlpatterns = [
    # incomming tag is /eut/

    #
    #  Eut URLs
    # ~~~~~~~~~~~~~~~
    url(r'^$',   views.Overview_Index.as_view(), name='home'),

    # url(r'^eut/(?P<pk>[0-9]+)/$',       views.EutDetailView.as_view(), name='eut_detail'),
    # url(r'^eut/add/$',                  views.EutCreate.as_view() , name='eut_create'),
]
