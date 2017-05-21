from django.contrib import admin
from .models import Todo, TodoPriorityLevel
# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoPriorityLevel)
