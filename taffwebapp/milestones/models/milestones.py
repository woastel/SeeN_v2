from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from system.models import System
from components.models import Component


class milestone(models.Model):
    objects = InheritanceManager()
    milestone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    information = models.TextField(max_length=5000)
    # Dates
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    # User
    user_creation = models.ForeignKey(User, related_name="88duf9guudfgh+")
    user_update = models.ForeignKey(User, related_name="234fdg243gf3+")


class milestone_task(models.Model):
    objects = InheritanceManager()
    ms_task_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    information = models.TextField(max_length=5000)
    # Dates
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    # User
    user_creation = models.ForeignKey(User, related_name="884jh56lz4igdrfz+")
    user_update = models.ForeignKey(User, related_name="aseawerwejkzughjfghhncvb+")
    milestone = models.ForeignKey(milestone)


class milestone_system_connection(models.Model):
    id_sc = models.AutoField(primary_key= True)
    milestone_var = models.ForeignKey(milestone)
    system_var = models.ForeignKey(System)

class milestone_component_connection(models.Model):
    id_cc = models.AutoField(primary_key= True)
    milestone_var = models.ForeignKey(milestone)
    component_var = models.ForeignKey(Component)
