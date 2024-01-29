from django.db import models


class Comment(models.Model):
    is_answer = models.BooleanField(
        default=False,
        verbose_name='Является ответом'
    )
    text = models.TextField(
        verbose_name='Комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments_post',
        verbose_name='Пост'
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='comments_user',
        verbose_name='Автор комментария'
    )
    # ссылка на комментарий для которого текущий коммент является ответом
    answer = models.ForeignKey(
        # II вар- 'Comment'
        'self',
        on_delete=models.CASCADE,
        related_name='answers',
        blank=True,
        null=True,
        verbose_name='Ответ'
    )

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
