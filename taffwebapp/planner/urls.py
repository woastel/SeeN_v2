from django.conf.urls import url
from planner.views import planner


app_name = 'planner'



urlpatterns = [
    # incomming tag is /eut/

    url(r'^index/$',                planner.IndexView.as_view(),            name='index'),
    url(r'^createSchedule/$',       planner.CreateSchedule.as_view(),       name='create_schedule'),
    url(r'^schedule_list/$',        planner.ScheduleListView.as_view(),     name='schedule_list'),
    url(r'^scheduleDetailView/(?P<pk>[0-9]+)/$',   planner.ScheduleDetailView.as_view(),   name='schedule_detail'),
    url(r'^scheduleDetailView/(?P<pk>[0-9]+)/(?P<danger>[-\w]+)$',   planner.ScheduleDetailView.as_view(),   name='schedule_detail_with_danger'),
    url(r'^scheduleDetailView/(?P<pk>[0-9]+)/(?P<success>[-\w]+)$',   planner.ScheduleDetailView.as_view(),   name='schedule_detail_with_success'),
    ]
