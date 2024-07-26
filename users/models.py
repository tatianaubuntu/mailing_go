from django.contrib.auth.models import AbstractUser
from django.db import models

from client.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            (
                'set_not_active',
                'May block users'
            )
        ]
        