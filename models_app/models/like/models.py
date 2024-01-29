from django.db import models


class Like(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='likes_post',
        verbose_name='Пост'
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='likes_user',
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f"{self.post.title}-{self.user}"

    class Meta:
        db_table = 'likes'
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
