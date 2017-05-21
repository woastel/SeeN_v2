from django.conf.urls import url
from . import views


app_name = 'components'

urlpatterns = [
    # incomming tag is /eut/

    url(r'^index/$',                     views.MainView.as_view() , name='index'),
    url(r'^complist/$',                  views.List_Component_View.as_view() , name='component_list'),
    url(r'^comp/(?P<pk>[0-9]+)/$',       views.Detail_Component_View.as_view(), name='component_detail'),

    # Create types (only used by admin )
    #url(r'^comp/componentType/add/$',   views.Create_Component_Type_View.as_view() ,       name='create_componentType'),
    url(r'^comp/Vendor/add/$',          views.Create_Vendor_View.as_view() ,  name='create_vendor'),

    # Chassis Component Views
    url(r'^comp/chassis/add/$',                         views.Create_Chassis_View.as_view(),        name='create_chassis'),
    url(r'^comp/chassis/update/(?P<pk>[0-9]+)/$',       views.Update_Chassis_View.as_view(),        name='update_chassis'),
    url(r'^comp/chassis/delete/(?P<pk>[0-9]+)/$',       views.Delete_Chassis_View.as_view(),        name='delete_chassis'),

    # Chassis Add On Component Views
    url(r'^comp/chassisAddOn/add/$',                    views.Create_ChassisAddOn_View.as_view(),   name='create_chassisAddOn'),
    url(r'^comp/chassisAddOn/update/(?P<pk>[0-9]+)/$',  views.Update_ChassisAddOn_View.as_view(),   name='update_chassisAddOn'),
    url(r'^comp/chassisAddOn/delete/(?P<pk>[0-9]+)/$',  views.Delete_ChassisAddOn_View.as_view(),   name='delete_chassisAddOn'),

    # Motherboard Component Views
    url(r'^comp/motherboard/add/$',                     views.Create_Motherboard_View.as_view(),   name='create_motherboard'),
    url(r'^comp/motherboard/update/(?P<pk>[0-9]+)/$',   views.Update_Motherboard_View.as_view(),   name='update_motherboard'),
    url(r'^comp/motherboard/delete/(?P<pk>[0-9]+)/$',   views.Delete_Motherboard_View.as_view(),   name='delete_motherboard'),

    # CPU Component Views
    url(r'^comp/cpu/add/$',                             views.Create_CPU_View.as_view() ,           name='create_cpu'),
    url(r'^comp/cpu/update/(?P<pk>[0-9]+)/$',           views.Update_CPU_View.as_view(),            name='update_cpu'),
    url(r'^comp/cpu/delete/(?P<pk>[0-9]+)/$',           views.Delete_CPU_View.as_view(),            name='delete_cpu'),

    # Memory Component Views
    url(r'^comp/memory/add/$',                          views.Create_Memory_View.as_view() ,        name='create_memory'),
    url(r'^comp/memory/update/(?P<pk>[0-9]+)/$',        views.Update_Memory_View.as_view(),         name='update_memory'),
    url(r'^comp/memory/delete/(?P<pk>[0-9]+)/$',        views.Delete_Memory_View.as_view(),         name='delete_memory'),

    # PSU Component Views
    url(r'^comp/psu/add/$',                             views.Create_PSU_View.as_view() ,           name='create_psu'),
    url(r'^comp/psu/update/(?P<pk>[0-9]+)/$',           views.Update_PSU_View.as_view(),            name='update_psu'),
    url(r'^comp/psu/delete/(?P<pk>[0-9]+)/$',           views.Delete_PSU_View.as_view(),            name='delete_psu'),

    # HDD Component Views
    url(r'^comp/hdd/add/$',                             views.Create_HDD_View.as_view() ,           name='create_hdd'),
    url(r'^comp/hdd/update/(?P<pk>[0-9]+)/$',           views.Update_HDD_View.as_view(),            name='update_hdd'),
    url(r'^comp/hdd/delete/(?P<pk>[0-9]+)/$',           views.Delete_HDD_View.as_view(),            name='delete_hdd'),

    # Heat Sink Component Views
    url(r'^comp/heatsink/add/$',                        views.Create_HeatSink_View.as_view() ,      name='create_heatsink'),
    url(r'^comp/heatsink/update/(?P<pk>[0-9]+)/$',      views.Update_HeatSink_View.as_view(),       name='update_heatsink'),
    url(r'^comp/heatsink/delete/(?P<pk>[0-9]+)/$',      views.Delete_HeatSink_View.as_view(),       name='delete_heatsink'),

    # FAN Component Views
    url(r'^comp/fan/add/$',                             views.Create_Fan_View.as_view() ,           name='create_fan'),
    url(r'^comp/fan/update/(?P<pk>[0-9]+)/$',           views.Update_Fan_View.as_view(),            name='update_fan'),
    url(r'^comp/fan/delete/(?P<pk>[0-9]+)/$',           views.Delete_Fan_View.as_view(),            name='delete_fan'),

    # Cable Component Views
    url(r'^comp/cable/add/$',                           views.Create_Cable_View.as_view() ,         name='create_cable'),
    url(r'^comp/cable/update/(?P<pk>[0-9]+)/$',         views.Update_Cable_View.as_view(),          name='update_cable'),
    url(r'^comp/cable/delete/(?P<pk>[0-9]+)/$',         views.Delete_Cable_View.as_view(),          name='delete_cable'),

    # PCBA Component Views
    url(r'^comp/pcba/add/$',                            views.Create_Pcba_View.as_view() ,          name='create_pcba'),
    url(r'^comp/pcba/update/(?P<pk>[0-9]+)/$',          views.Update_Pcba_View.as_view(),           name='update_pcba'),
    url(r'^comp/pcba/delete/(?P<pk>[0-9]+)/$',          views.Delete_Pcba_View.as_view(),           name='delete_pcba'),

    # PCIe Ctrl Component Views
    url(r'^comp/pciectrl/add/$',                        views.Create_PcieCtrl_View.as_view() ,      name='create_pciectrl'),
    url(r'^comp/pciectrl/update/(?P<pk>[0-9]+)/$',      views.Update_PcieCtrl_View.as_view(),       name='update_pciectrl'),
    url(r'^comp/pciectrl/delete/(?P<pk>[0-9]+)/$',      views.Delete_PcieCtrl_View.as_view(),       name='delete_pciectrl'),
    ]
