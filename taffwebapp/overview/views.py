from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views import generic, View
from django.views.generic import base
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from todos.models import TodoAllocated
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class Overview_Index(base.TemplateView):

    template_name = 'overview/index.html'


    def get_context_data(self, **kwargs):
        # Standard init with super()
        context = super(Overview_Index, self).get_context_data(**kwargs)

        context["username"] = self.request.user.username

        a = TodoAllocated.objects.filter(   Q(user__username=context['username']),
                                            Q(status_done=False))
        context["todos_open"] = a.count()

        #############
        #  Debug
        #############

        for i in a:
            print(i)



        #############
        #  Debug ENDE
        #############


        # data modeling
        current_user = self.request.user
        print(current_user.username)

        # add data to context
        context["username"] = current_user.username

        # return the context
        return context
