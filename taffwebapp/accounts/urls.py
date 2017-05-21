from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    # incomming tag is /eut/

    #
    #  Eut URLs
    # ~~~~~~~~~~~~~~~
    url(r'^login/',   views.login_view, name='login'),
    url(r'^logout/',   views.logoout_view, name='logout'),
    url(r'^register/',   views.register_view, name='register'),
    url(r'^about/',   views.about_view, name='about'),
    #url(r'^register/$',   views.UserFormView_Registration.as_view(), name='register'),
    # url(r'^eut/(?P<pk>[0-9]+)/$',       views.EutDetailView.as_view(), name='eut_detail'),
    # url(r'^eut/add/$',                  views.EutCreate.as_view() , name='eut_create'),
]
