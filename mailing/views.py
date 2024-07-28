from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailing.forms import SettingsModeratorForm, SettingsForm
from mailing.models import Settings


class SettingsListView(LoginRequiredMixin, ListView):
    model = Settings
    extra_context = {
        'title': 'Рассылки'
    }


class SettingsDetailView(LoginRequiredMixin, DetailView):
    model = Settings
    extra_context = {
        'title': 'Рассылка'
    }


class SettingsCreateView(LoginRequiredMixin, CreateView):
    model = Settings
    fields = ('first_mailing_date', 'frequency', 'status', 'message', 'client',)
    extra_context = {
        'title': 'Форма по добавлению'
    }

    def get_success_url(self):
        return reverse('mailing:settings_list')

    def form_valid(self, form):
        settings = form.save()
        user = self.request.user
        settings.owner = user
        settings.save()
        return super().form_valid(form)


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Settings
    fields = ('first_mailing_date', 'frequency', 'status', 'message', 'client',)
    form_class = SettingsForm
    extra_context = {
        'title': 'Форма по редактированию'
    }

    def get_success_url(self):
        return reverse('mailing:settings_detail',
                       args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user == self.object.owner:
            return SettingsForm
        elif user.has_perm('mailing.set_status_to_completed'):
            return SettingsModeratorForm
        raise PermissionDenied


class SettingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Settings
    extra_context = {
        'title': 'Удаление рассылки'
    }
    success_url = reverse_lazy('mailing:settings_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user or self.request.user.is_superuser
