from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from system.models import System as system_system
# from system.models import msdbData


class Schedule(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    created_user = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    system = models.ForeignKey(system_system)

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')


class Certification_Type(models.Model):
    name = models.CharField(max_length=100)
    estimated_days = models.PositiveIntegerField()

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')


class ScheduleItem_Certification(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    created_user = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    estimated_end_date = models.DateTimeField()
    certificatio_type = models.ForeignKey(Certification_Type)
    schedule = models.ForeignKey(Schedule)

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')


class Measurement_Type(models.Model):
    name = models.CharField(max_length=100)
    estimated_days = models.PositiveIntegerField()

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')


class ScheduleItem_Measurement(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    created_user = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    estimated_end_date = models.DateTimeField()
    measurement_type = models.ForeignKey(Measurement_Type)
    schedule = models.ForeignKey(Schedule)

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')


class ScheduleItem_Material(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    created_user = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    schedule = models.ForeignKey(Schedule)

    def __str__(self):
        return(str(self.id) + " - " + self.name)

    def get_absolute_url(self):
        return reverse('schedule:index')
