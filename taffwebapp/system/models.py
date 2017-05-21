from django.db import models
from django.contrib.auth.models import User
from components.models import Component



class SystemModel(models.Model):
    """
        SystemModel - (Model):
            z.b: RX-2U-D   = rx 2u dual socket server
            z.b: TX-1U-M   = tx 1u mono server

            --> abbildung des portfolios
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class System(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=5000)
    model = models.ForeignKey(SystemModel, on_delete=models.PROTECT)
    owner = models.ForeignKey(User)
    owner_co = models.ForeignKey(User, related_name="cocococococco")

    def __str__(self):
        return str("id " + str(self.id) + " - " + self.name)


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    creator = models.ForeignKey(User)
    createtion_date = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class MSDBConnention(models.Model):
    # z.B.: MS10, MS20, MS25, MS30,
    system = models.ForeignKey(System)
    milestone = models.ForeignKey(Milestone)
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    milestoneFinish_date = models.DateTimeField() # soll das datum sein an dem der Milestone erreicht wwerden soll

    def __str__(self):
        return (str(self.id) + " - " + str(self.system.name) + " - " + str(self.milestone.name))



# Noch nicht eingebaut
class System_Component_connection(models.Model):
    user_creator = models.ForeignKey(User)
    date_creation = models.DateTimeField()

    component_count = models.PositiveIntegerField()
    component = models.ForeignKey(Component)
    system = models.ForeignKey(System)

    def __str__(self):
        return(
                str(self.id) + " - " +
                str(self.system.name) + " - " +
                str(self.component.name)
                )
