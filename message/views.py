from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from message.models import Message


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения'
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    extra_context = {
        'title': 'Сообщение'
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject', 'text',)
    extra_context = {
        'title': 'Форма по добавлению'
    }

    def get_success_url(self):
        return reverse('client:client_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    permission_required = 'message.change_message'
    fields = ('subject', 'text',)
    extra_context = {
        'title': 'Форма по редактированию'
    }

    def get_success_url(self):
        return reverse('message:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    permission_required = 'message.delete_message'
    extra_context = {
        'title': 'Удаление сообщения'
    }
    success_url = reverse_lazy('message:message_list')
