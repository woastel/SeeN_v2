from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
    # incomming tag is /todos/

    url(r'^$', views.Todo_MainView.as_view(), name='main'),

    #
    #  Todo URLs
    # ~~~~~~~~~~~~~~~
    url(r'^todos/$', views.Todo_ListView.as_view(), name='todos_list'),

    url(r'^todos/(?P<pk>[0-9]+)/$', views.Todo_DetailView.as_view(), name='todos_detail'),

    url(r'^todos/add/$', views.Todo_Create.as_view(), name='todos_create2'),

    url(r'^todos/(?P<pk>[0-9]+)/update/$', views.Todo_Update.as_view(), name='todos_update'),

    url(r'^todos/(?P<pk>[0-9]+)/delete/$', views.Todo_Delete.as_view(), name='todos_delete'),

    #
    #  Todo List URLs
    # ~~~~~~~~~~~~~~~
    url(r'^todosallocated/$', views.TodoAllocated_ListView.as_view(), name='todos_allocated_list'),

    url(r'^todosallocated/(?P<pk>[0-9]+)/update/$', views.TodoAllocated_Update.as_view(), name='todos_allocated_update'),

    #
    #  Todo Status URLs
    # ~~~~~~~~~~~~~~~
    url(r'^todosstatus/$', views.Todo_Status_List.as_view(), name='todos_status_list'),

    url(r'^todosstatus/(?P<pk>[0-9]+)/update/$', views.Todo_Status_Detail.as_view(), name='todos_status_detail_update'),




    #
    #  Old URLs
    # ~~~~~~~~~~~~~~~

    # url(r'^todos/system/(?P<system_id>[0-9]+)/$',
    #     views.TodoListViewBySystem.as_view(),
    #     name='todos_list_system'),
    ]
