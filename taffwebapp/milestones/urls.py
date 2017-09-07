from django.conf.urls import url
from . import views

from milestones.views import ()

app_name = 'milestones'

urlpatterns = [
    # Measurement (general) Views
    url(r'^milestones/$',          view_measurement.IndexView.as_view() ,                          name='index'),

]
