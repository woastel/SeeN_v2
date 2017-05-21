from django.conf.urls import url
from . import views

app_name = 'schedule'

urlpatterns = [
    # incomming tag is /eut/

    url(r'^schedule/$',                                         views.MainView.as_view(),                               name='index'),

    url(r'^create/scheduel$',                                   views.Create_Schedule_View.as_view(),                   name='create_schedule'),
    url(r'^update/scheduel/(?P<pk>[0-9]+)/$',                   views.Update_Schedule_View.as_view(),                   name='update_schedule'),
    url(r'^delete/scheduel/(?P<pk>[0-9]+)/$',                   views.Delete_Schedule_View.as_view(),                   name='delete_schedule'),

    url(r'^create/certificationtype$',                          views.Create_CertificationType_View.as_view(),          name='create_certification_type'),
    url(r'^update/certificationtype/(?P<pk>[0-9]+)/$',          views.Update_CertificationType_View.as_view(),          name='update_certification_type'),
    url(r'^delete/certificationtype/(?P<pk>[0-9]+)/$',          views.Delete_CertificationType_View.as_view(),          name='delete_certification_type'),

    url(r'^create/scheduleitemcertification$',                  views.Create_ScheduleItemCertification_View.as_view(),  name='create_schedule_item_certification'),
    url(r'^update/scheduleitemcertification/(?P<pk>[0-9]+)/$',  views.Update_ScheduleItemCertification_View.as_view(),  name='update_schedule_item_certification'),
    url(r'^delete/scheduleitemcertification/(?P<pk>[0-9]+)/$',  views.Delete_ScheduleItemCertification_View.as_view(),  name='delete_schedule_item_certification'),

    url(r'^create/measurementtype$',                            views.Create_MeasurementType_View.as_view(),            name='create_measurement_type'),
    url(r'^update/measurementtype/(?P<pk>[0-9]+)/$',            views.Update_MeasurementType_View.as_view(),            name='update_measurement_type'),
    url(r'^delete/measurementtype/(?P<pk>[0-9]+)/$',            views.Delete_MeasurementType_View.as_view(),            name='delete_measurement_type'),

    url(r'^create/scheduleitemmeasurement$',                    views.Create_ScheduleItemMeasurement_View.as_view(),    name='create_schedule_item_measurement'),
    url(r'^update/scheduleitemmeasurement/(?P<pk>[0-9]+)/$',    views.Update_ScheduleItemMeasurement_View.as_view(),    name='update_schedule_item_measurement'),
    url(r'^delete/scheduleitemmeasurement/(?P<pk>[0-9]+)/$',    views.Delete_ScheduleItemMeasurement_View.as_view(),    name='delete_schedule_item_measurement'),

    url(r'^create/scheduleitemmaterial$',                       views.Create_ScheduleItemMaterial_View.as_view(),       name='create_schedule_item_material'),
    url(r'^update/scheduleitemmaterial/(?P<pk>[0-9]+)/$',       views.Update_ScheduleItemMaterial_View.as_view(),       name='update_schedule_item_material'),
    url(r'^delete/scheduleitemmaterial/(?P<pk>[0-9]+)/$',       views.Delete_ScheduleItemMaterial_View.as_view(),       name='delete_schedule_item_material'),

    url(r'^view/allobjects$',                                   views.View_Schedule_objects.as_view(),                  name='view_all_objects'),
    # url(r'^view/aSchedule/(?P<scheduleid>[0-9]+)$',           views.View_a_schedule.as_view(),                        name='view_a_Schedule'),
    url(r'^view/aSchedule/(?P<schedule_id>[0-9]+)/$',           views.View_a_schedule.as_view(),                        name='view_a_Schedule'),

    # url(r'^eut/(?P<pk>[0-9]+)/$',       views.EutDetailView.as_view(), name='eut_detail'),
    # url(r'^eut/add/$',                  views.EutCreate.as_view() , name='eut_create'),
]
