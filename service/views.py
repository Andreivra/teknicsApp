from django.shortcuts import render
from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from service.forms import TaskForm, TaskUpdateForm
from service.models import Company


class ServiceTaskCreateView(SuccessMessageMixin, CreateView):
    template_name = 'service/create_service_task.html'
    model = Company
    form_class = TaskForm
    success_url = reverse_lazy('list-of-tasks')
    success_message = "Task-ul companiei {company_name} a fost creat cu success"
    permission_required = 'task.add_task'

    def form_valid(self, form):
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.company_name = new_task.company_name.title()
            new_task.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(company_name=self.object.company_name)


class ServiceTaskListView(ListView):
    template_name = 'service/list_of_tasks.html'
    model = Company
    context_object_name = 'all_tasks'
    permission_required = 'task.view_task_list'

    def get_queryset(self):
        return Company.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.now()
        data['current_date_time'] = now
        return data


class ServiceTaskDetailsView(DetailView):
    template_name = 'service/task_details.html'
    model = Company
    success_url = reverse_lazy('list-of-tasks')
    permission_required = 'task.view_task'


class ServiceTaskUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'service/update_task.html'
    model = Company
    form_class = TaskUpdateForm
    success_url = reverse_lazy('list-of-tasks')
    success_message = "Task-ul %(company_name_field)s a fost actualizat cu success  "
    permission_required = 'task.change_task'
    permission_denied_message = 'Permission denied today'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            company_name_field=self.object.company_name,
        )


class ServiceTaskDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'service/delete_task.html'
    model = Company
    success_url = reverse_lazy('list-of-tasks')
    success_message = "Task-ul companiei %(company_name_field)s a fost sters cu success "
    permission_required = 'task.task_delete'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            company_name_field=self.object.company_name,
        )
