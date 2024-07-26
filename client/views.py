from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from client.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Клиенты'
    }


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': 'Клиент'
    }


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'comment',)
    extra_context = {
        'title': 'Форма по добавлению'
    }

    def get_success_url(self):
        return reverse('client:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'comment',)
    extra_context = {
        'title': 'Форма по редактированию'
    }

    def get_success_url(self):
        return reverse('client:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    extra_context = {
        'title': 'Удаление клиента'
    }
    success_url = reverse_lazy('client:client_list')
