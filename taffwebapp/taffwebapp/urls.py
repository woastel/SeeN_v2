"""taffwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r'^eut/', include('eut.urls')),
    url(r'^system/', include('system.urls')),
    url(r'^todos/', include('todos.urls')),
    url(r'^climaticmeasurement/', include('climaticmeasurement.urls')),
    url(r'^measurement/', include('measurement.urls')),

    url(r'^schedule/', include('schedule.urls')),
    url(r'^comp/', include('components.urls')),
    url(r'', include('overview.urls')),

    url(r'^admin/', admin.site.urls),
]
