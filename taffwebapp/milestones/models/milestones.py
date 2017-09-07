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
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    user_creation = models.ForeignKey(User, related_name="884jh56lz4igdrfz+")
    user_update = models.ForeignKey(User, related_name="aseawerwejkzughjfghhncvb+")

    date_delivery = models.DateTimeField()
    # wenn dieses Flag True ist dann wurde der Milestone erreicht
    #   dieses Flag kann auch automatisch anhand des date_delivery Datums gesetzt werden
    ms_done = models.BooleanField(default=False)

class milestone_component_connection(models.Model):
    id_cc = models.AutoField(primary_key= True)
    milestone_var = models.ForeignKey(milestone)
    component_var = models.ForeignKey(Component)
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    user_creation = models.ForeignKey(User, related_name="884jh56lz4igdrfz+")
    user_update = models.ForeignKey(User, related_name="aseawerwejkzughjfghhncvb+")

    date_delivery = models.DateTimeField()
    # wenn dieses Flag True ist dann wurde der Milestone erreicht
    #   dieses Flag kann auch automatisch anhand des date_delivery Datums gesetzt werden
    ms_done = models.BooleanField(default=False)


class milestone_task_system_conection_tracker(models.Model):
    id_cc = models.AutoField(primary_key= True)
    milestone_task_x = models.ForeignKey(milestone_task)
    milestone_system_conni = models.ForeignKey(milestone_system_connection)
    ms_task_done = models.BooleanField(default=False)
    ms_task_done_date =models.DateTimeField()

class milestone_task_component_connection_tracker(models.Model):
    id_mtcct = models.AutoField(primary_key= True)
    milestone_task_x = models.ForeignKey(milestone_task)
    milestone_component_conni = models.ForeignKey(milestone_component_connection)
    ms_task_done = models.BooleanField(default=False)
    ms_task_done_date =models.DateTimeField()
