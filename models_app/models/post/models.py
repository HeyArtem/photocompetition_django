from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        help_text='Впишите заголовок',
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        verbose_name='Слаг'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    description = models.TextField(
        verbose_name='Текст поста'
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        related_name='posts_status',
        verbose_name='Статус поста'
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='posts_user',
        verbose_name='Автор поста'
    )

    def __str__(self):
        return f"{self.id}-{self.slug}"


    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'slug_post': self.slug})

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

        # Индексирование
        indexes = [
            models.Index(fields=['-updated_at']),
        ]
