from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from client.models import Client
from client.services import get_cashe_blog_list
from mailing.models import Settings


class StatisticTemplateView(TemplateView):
    template_name = 'client/statistic.html'
    extra_context = {
        'title': 'Статистика'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing_count'] = get_cashe_blog_list()[1]
        context_data['active_mailing_count'] = Settings.objects.filter(status='запущена').count()
        context_data['blog_list'] = get_cashe_blog_list()[0]
        context_data['clients_count'] = Client.objects.all().count()
        return context_data


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


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'comment',)
    extra_context = {
        'title': 'Форма по редактированию'
    }

    def get_success_url(self):
        return reverse('client:client_detail',
                       args=[self.kwargs.get('pk')])

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_superuser


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    extra_context = {
        'title': 'Удаление клиента'
    }
    success_url = reverse_lazy('client:client_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_superuser
