from django.conf.urls import url
from . import views

from milestones.views import milestones

app_name = 'milestones'

urlpatterns = [
    # Measurement (general) Views
    url(r'^milestones/$',          milestones.IndexView.as_view() ,                          name='index'),
    url(r'^createMilestone/$',          milestones.Create_Milestone.as_view() ,                          name='create_milestone'),
]
