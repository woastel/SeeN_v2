from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from datetime import datetime

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))


# Component Table
class Component(models.Model):

    objects = InheritanceManager()
    # component id is the (pk) auto
    component_id = models.AutoField(primary_key=True)

    # name of the component
    name = models.CharField(max_length=100)

    # Component Type Text - will set by the save function in the individual components
    component_type_text = models.CharField(max_length=100, default="Component")
    # component Vendor
    vendor = models.ForeignKey(Vendor, models.SET_NULL, null=True)
    # Informations about the component
    information = models.TextField(max_length=5000)

    # date time and user - not accesible in form (automatic generation)
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    user_creator = models.ForeignKey(User)
    user_updater= models.ForeignKey(User, related_name='%(class)s_requests_created')

    # delivery date -- is the estimated delivery date
    #   this date is relevant for the schedule
    delivery_date = models.DateTimeField()


    # Character avalible
    character_mechanical_avalible = models.BooleanField(default=False)
    character_electrical_avalible = models.BooleanField(default=False)
    character_thermal_avalible = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.component_type_text) + ": " +
                str(self.name))


# abstract models for specified components
class Component_Character_Mechanical(models.Model):
    #character_mechaical_id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=100)
    size_x = models.DecimalField(max_digits=10, decimal_places=2)
    size_y = models.DecimalField(max_digits=10, decimal_places=2)
    size_z = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class Component_Character_Electrical_Power(models.Model):
    #character_electrical_id = models.AutoField(primary_key=True)
    power_max = models.DecimalField(max_digits=10, decimal_places=2)
    power_typical = models.DecimalField(max_digits=10, decimal_places=2)
    power_minimal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class Component_Character_Thermal(models.Model):
    #character_thermal_id = models.AutoField(primary_key=True)
    temperature_max = models.IntegerField()
    airflow_min = models.IntegerField()

    class Meta:
        abstract = True


# Component Tables Specified
class Chassis       (Component, Component_Character_Mechanical):
    model = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools

        print(self.user_updater)

        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "Chassis"
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class ChassisAddOn  (Component, Component_Character_Mechanical):
    model = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "Chassis Add On"
        # Call the Super Methode
        super(ChassisAddOn, self).save(*args, **kwargs)

class Motherboard   (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    pcie_slot_count = models.PositiveIntegerField()
    cpu_slot_count = models.PositiveIntegerField()
    psu_slot_count = models.PositiveIntegerField()
    memory_slot_count = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "Motherboard"
        # Call the Super Methode
        super(Motherboard, self).save(*args, **kwargs)

class Cpu           (Component, Component_Character_Electrical_Power, Component_Character_Thermal):
    cores = models.IntegerField()
    TDP = models.FloatField()
    frequency = models.FloatField()
    klasse = models.FloatField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = False
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "CPU"
        # Call the Super Methode
        super(Cpu, self).save(*args, **kwargs)

class Memory        (Component, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.IntegerField()
    ddr_version = models.CharField(max_length=100)
    speed_frequency = models.FloatField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = False
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "Memory"
        # Call the Super Methode
        super(Memory, self).save(*args, **kwargs)

class PSU           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    power_class = models.CharField(max_length=100)
    formfactor = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "PSU"
        # Call the Super Methode
        super(PSU, self).save(*args, **kwargs)

class HDD           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.PositiveIntegerField()
    technology = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "HDD"
        # Call the Super Methode
        super(HDD, self).save(*args, **kwargs)

class HeatSink      (Component, Component_Character_Mechanical):
    technology = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "Heat Sink"
        # Call the Super Methode
        super(HeatSink, self).save(*args, **kwargs)

class Fan           (Component, Component_Character_Mechanical):
    maximum_rpm = models.IntegerField()
    maximum_airflow = models.IntegerField()
    maximum_pressure = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "Fan"
        # Call the Super Methode
        super(Fan, self).save(*args, **kwargs)

class Cable         (Component, Component_Character_Mechanical):
    cable_type = models.CharField(max_length=100)
    lenght = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "Cable"
        # Call the Super Methode
        super(Cable, self).save(*args, **kwargs)

class Pcba          (Component, Component_Character_Mechanical):
    pcba_type = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        self.component_type_text = "PCBA"
        # Call the Super Methode
        super(Pcba, self).save(*args, **kwargs)

class Pcie_Ctrl     (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    pcie_spec = models.IntegerField()
    pcie_lanes_electrical = models.IntegerField()
    pcie_lanes_mechanical = models.IntegerField()
    pcie_ctrl_type = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        self.component_type_text = "PCIe Controller"
        # Call the Super Methode
        super(Pcie_Ctrl, self).save(*args, **kwargs)
