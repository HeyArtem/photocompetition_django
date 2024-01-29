from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='users/avatar/', verbose_name='Аватар'
    )

    def __str__(self):
        return self.username

    # Кнопка "Смотреть на сайте" в админке(Изменить пользователя)
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        # Сортировка в админке (& listView) по дате регистрации (в обр-ом порядке), дальше по Имени
        # Но я сделаю в админке
        # ordering = ['-date_joined', 'username']

