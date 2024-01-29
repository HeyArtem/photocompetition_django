from django.db import models


class Picture(models.Model):
    current = models.BooleanField(
        default=False,
        verbose_name='Основная или вторичная'
    )
    image = models.ImageField(
        upload_to='pictures/image/%Y/%m/%d',
        verbose_name='Картинка'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='pictures',
        verbose_name='Пост'
    )

    def __str__(self):
        return f"{self.current}-{self.post.title}"

    class Meta:
        db_table = 'pictures'
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
