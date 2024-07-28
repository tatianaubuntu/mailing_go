from django.db import models

from client.models import NULLABLE


class Message(models.Model):
    subject = models.CharField(max_length=150,
                               verbose_name='тема письма')
    text = models.TextField(verbose_name='текст сообщения')

    owner = models.ForeignKey('users.User',
                              on_delete=models.SET_NULL,
                              help_text='Укажите владельца',
                              **NULLABLE)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
