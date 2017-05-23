from django.conf.urls import url
from planner.views import planner


app_name = 'planner'



urlpatterns = [
    # incomming tag is /eut/

    url(r'^index/$',                     planner.IndexView.as_view() , name='index'),

    ]
