from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import collections

# from system.models import msdbName as system_msdb_name
from system.models import System as system_system



class TodoPriorityLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.id) + " : " + str(self.name))

class Todo(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    priorityLevel = models.ForeignKey(TodoPriorityLevel, on_delete=models.PROTECT)
    createtion_date = models.DateTimeField()
    creator = models.ForeignKey(User)
    must_done_date = models.DateTimeField()
    public = models.BooleanField(default=False)
    # status_done = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.id) + " : " + str(self.name))

    def get_absolute_url(self):
        return reverse('todos:todos_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        flag = False
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk
            temp = self
            flag = True

        super(Todo, self).save(*args, **kwargs)

        if flag is True:
            if self.public is True:
                users = User.objects.all()

                for i in users:
                    todoListEntry = TodoAllocated()
                    todoListEntry.todo = temp
                    todoListEntry.user = i
                    todoListEntry.must_done_date = temp.must_done_date
                    todoListEntry.status_done = False
                    todoListEntry.save()



            elif self.public is False:
                todoListEntry = TodoAllocated()
                todoListEntry.todo = temp
                todoListEntry.user = temp.creator
                todoListEntry.must_done_date = temp.must_done_date
                todoListEntry.status_done = False
                todoListEntry.save()

        flag = False

class TodoAllocated(models.Model):
    todo = models.ForeignKey(Todo)
    user = models.ForeignKey(User)
    must_done_date = models.DateTimeField()
    status_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        # kann geändert werden wenn nach dem erstellen doch lieber die details
        # angeschaut werden sollen
        # return reverse('todos:todos_detail', kwargs={'pk': self.pk})
        return reverse('todos:todos_allocated_list')
