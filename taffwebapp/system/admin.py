from django.contrib import admin
from .models import System, Milestone, SystemModel, MSDBConnention
# Register your models here.
admin.site.register(System)
admin.site.register(Milestone)
admin.site.register(MSDBConnention)
admin.site.register(SystemModel)
