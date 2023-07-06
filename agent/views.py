# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# from trainer.filters import TrainerFilters
from agent.models import Agent
from agent.forms import AgentForm, AgentUpdateForm
from datetime import datetime


class AgentCreateView(CreateView):
    template_name = 'agent/create_agent.html'
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('list-of-agents')
    success_message = "Agentul {first_name} {last_name} a fost creat cu success"
    permission_required = 'agent.add_agent'

    def form_valid(self, form):
        if form.is_valid():
            new_agent = form.save(commit=False)
            new_agent.first_name = new_agent.first_name.title()
            new_agent.last_name = new_agent.last_name.title()
            new_agent.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(first_name=self.object.first_name, last_name=self.object.last_name)


class AgentListView(ListView):
    template_name = 'agent/list_of_agents.html'
    model = Agent
    context_object_name = 'all_agents'
    permission_required = 'agent.view_list_of_agents'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.now()
        data['current_date_time'] = now
        return data
