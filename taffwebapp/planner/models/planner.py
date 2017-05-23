from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from system.models import System
from components.models import Component






class schedule(models.Model):

    name = models.CharField(max_length=100)
    information = models.TextField(max_length=5000)

    # Dates
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()

    # User
    user_creation = models.ForeignKey(User, related_name="asdfkljasnuhsdfgnwlereationaaaa")
    user_update = models.ForeignKey(User, related_name="uuuwuejrhkjfalsdfjpppaksdlk")

    # public field
    #   if public False only the creator can view this schedule
    #   if public True everybody can view this schedule
    public = models.BooleanField(default=False)

    # main_connection_avalible field
    #   bevor schedule items an einen schedule hinzugefuegt werden
    #   braucht der schedule eine main Connection
    #   das kann ein system oder eine componente sein
    #   - in den tables
    #       - schedule_system_connection
    #       - schedule_component_connection
    #   schliest aber nicht aus das mehrere systeme oder componente an eine
    #   schedule connectet werden koennen
    main_connection_avalible = models.BooleanField(default=False)


class scheduleItem(models.Model):

    objects = InheritanceManager()

    schedule_item_id = models.AutoField(primary_key=True)

    # Dates
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()

    # User
    user_creation = models.ForeignKey(User, related_name="schedule_item_creeation")
    user_update = models.ForeignKey(User, related_name="schedule_item_UUUPdate")

    #
    item_start_date_avalible = models.BooleanField(default=False)
    item_start_date = models.DateTimeField()
    item_end_date_avalible = models.BooleanField(default=False)
    item_end_date = models.DateTimeField()
    item_duration_avalible = models.BooleanField(default=False)
    item_duration = models.PositiveIntegerField()

    # wenn dieses Feld True ist dann soll in der schedule item depencis Tablle
    # nachgescht werden und die abhaengikeiten eingepflegt werden
    item_depencis_avalible = models.BooleanField(default=False)


class schedule_scheduleItem_connection(models.Model):
    schedule = models.ForeignKey(schedule)
    schedule_item = models.ForeignKey(scheduleItem)
    user_creation = models.ForeignKey(User)
    date_creation = models.DateTimeField()

    def delete(self, *args, **kwargs):
        self.schedule_item.delete()
        super(schedule_scheduleItem_connection, self).delete(*args, **kwargs)


class schedule_system_connection(models.Model):
    schedule = models.ForeignKey(schedule)
    system = models.ForeignKey(System)
    user_creation = models.ForeignKey(User)
    date_creation = models.DateTimeField()

    # is_a_main_connection
    #   wenn dieses Feld True ist dann darf der datensatz nicht geloescht werden
    is_a_main_connection = models.BooleanField(default=False)


class schedule_component_connection(models.Model):
    schedule = models.ForeignKey(schedule)
    component = models.ForeignKey(Component)
    user_creation = models.ForeignKey(User)
    date_creation = models.DateTimeField()

    # is_a_main_connection
    #   wenn dieses Feld True ist dann darf der datensatz nicht geloescht werden
    is_a_main_connection = models.BooleanField(default=False)
