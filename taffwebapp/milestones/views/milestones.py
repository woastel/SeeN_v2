from django.views import generic
from django.shortcuts import render



class IndexView(generic.View):
    template_name = 'milestones/index_.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)
