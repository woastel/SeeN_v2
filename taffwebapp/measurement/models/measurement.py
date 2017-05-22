from django.db import models
from django.contrib.auth.models import User
from eut.models import Eut
from model_utils.managers import InheritanceManager


class measurement(models.Model):

    objects = InheritanceManager()

    measurement_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    information = models.TextField(max_length=5000)

    # Dates
    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()

    # User
    user_creation = models.ForeignKey(User, related_name="measurementUserCreationaaaa")
    user_update = models.ForeignKey(User, related_name="measurementlalalallalaUpdateed")

    # EUT information
    eut = models.ForeignKey(Eut)

    # measurement result is pass
    # is true or false
    measurement_is_pass = models.BooleanField(default=False)

    # Measurement Type (as text info)
    #  this field will be set by the save methode
    measurement_type = models.CharField(max_length=100)

    public = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        print(self.eut.locked)
        eut_list = Eut.objects.filter(id=self.eut.id)
        eut = eut_list[0]
        eut.locked = True
        eut.save()

        print(self.eut.locked)

        super(measurement, self).save(*args, **kwargs)


    #def __str__(self):

    #    print(str(self.name) + " " + str(self.measurement_id))
