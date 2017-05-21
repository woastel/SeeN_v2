from datetime import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo, TodoAllocated
from . import forms



""" Main: View function """

@method_decorator(login_required, name='dispatch')
class Todo_MainView(generic.TemplateView):
    template_name = 'todos/todos_index.html'


""" Todo (Model): View function """

@method_decorator(login_required, name='dispatch')
class Todo_ListView(generic.ListView):
    model = Todo
    template_name = 'todos/todos_asTabel.html'

    def get_context_data(self, **kwargs):
        # first init the context from this view
        context = super(Todo_ListView, self).get_context_data(**kwargs)

        # Get the username of the aktuall logt in user
        context["username"] = self.request.user.username


        todo_list_for_tabel = Todo.objects.filter(Q(creator__username=context['username']))
        context['todo_list_for_tabel'] = reversed(todo_list_for_tabel)


        return context

@method_decorator(login_required, name='dispatch')
class Todo_DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/todos_detailview.html'

    def get_absolute_url(self):
        return reverse('todos:todos_detail', kwargs={'pk': self.pk})

@method_decorator(login_required, name='dispatch')
class Todo_Create(View):
    form_class = forms.ToDoForm
    template_name = "todos/todos_form.html"

    def get(self, request, *args, **kwargs):

        initial = {
            # 'user': request.user,
            'createtion_date': datetime.now(),
            # -- is a old option'status': 1,
            'priorityLevel': 5
            }

        form = self.form_class(initial=initial)
        context = {'form': form}
        return render(request, self.template_name , context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # set here the user of this ToDo object
            instance.creator = request.user
            # print(instance.user)
            instance.save()
            return HttpResponseRedirect('/todos/todos/')

@method_decorator(login_required, name='dispatch')
class Todo_Update(UpdateView):
    form_class = forms.ToDoForm
    model = Todo
    # fields = ["name", "text", "creator", "createtion_date", "priorityLevel",
    #             "status", "must_done_msdb", "must_done_date"]
    # template_name_suffix = '_update_form'
    template_name = "todos/todos_form.html"

@method_decorator(login_required, name='dispatch')
class Todo_Delete(DeleteView):
    model = Todo
    success_url = reverse_lazy("todos:todos_list")
    template_name = 'todos/todos_confirm_delete.html'


    def delete(self, request, *args, **kwargs):
        """
            Funktion to check the user
            only the creator can delete the object nobody else
        """

        # get the object you would be delete
        self.object = self.get_object()
        # check if the creator.username is the requested username
        if self.object.creator.username != request.user.get_username():
            # if not send a error
            return HttpResponse("FAIL not the right user")

        # store the success url
        success_url = self.get_success_url()
        # delete the object
        self.object.delete()
        # return the success url
        return HttpResponseRedirect(success_url)


""" TodoAllocated (Model): View function """

@method_decorator(login_required, name='dispatch')
class TodoAllocated_ListView(generic.ListView):
    model = Todo
    template_name = 'todos/todosAllocated_asTabel.html'


    def get_context_data(self, **kwargs):
        # first init the context from this view
        context = super(TodoAllocated_ListView, self).get_context_data(**kwargs)

        # Get the username of the aktuall logt in user
        context["username"] = self.request.user.username


        todo_list_for_tabel_new_open = TodoAllocated.objects.filter(
            Q(user__username=context['username']),
            Q(status_done=False))

        context['todo_list_for_tabel_new_open'] = reversed(
            todo_list_for_tabel_new_open)

        todo_list_for_tabel_new_done = TodoAllocated.objects.filter(
            Q(user__username=context['username']),
            Q(status_done=True))

        context['todo_list_for_tabel_new_done'] = reversed(
            todo_list_for_tabel_new_done)


        return context

@method_decorator(login_required, name='dispatch')
class TodoAllocated_Update(UpdateView):
    model = TodoAllocated
    fields = ["must_done_date", "status_done"]
    template_name = "todos/todos_form.html"

@method_decorator(login_required, name='dispatch')
class Todo_Status_List(generic.TemplateView):

    template_name = 'todos/todos_status_public_list.html'

    def get_context_data(self, **kwargs):
        # first init the context from this view
        context = super(Todo_Status_List, self).get_context_data(**kwargs)

        # Get the username of the aktuall logt in user
        context["username"] = self.request.user.username



        todo_list = Todo.objects.filter(Q(creator__username=context['username']))

        for i in todo_list:
            print(i)

        context['todo_list'] = reversed(todo_list)

        return context

@method_decorator(login_required, name='dispatch')
class Todo_Status_Detail(generic.TemplateView):
    template_name = 'todos/todos_status_public_detail.html'

    def get_context_data(self, **kwargs):
        # first init the context from this view
        context = super(Todo_Status_Detail, self).get_context_data(**kwargs)

        # Get the username of the aktuall logt in user
        context["username"] = self.request.user.username

        search_for_todo_id =  kwargs['pk']
        print(search_for_todo_id)

        todo_list = TodoAllocated.objects.filter(Q(todo__pk=search_for_todo_id))

        for i in todo_list:
            print("{} | {} | {} | {}".format(i.todo, i.user, i.must_done_date, i.status_done))

        context['todo_list'] = reversed(todo_list)

        return context

""" developer """


""" End Functions """
