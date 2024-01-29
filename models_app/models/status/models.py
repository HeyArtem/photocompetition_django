from django.db import models


class Status(models.Model):
    state = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Статус'
    )

    def __str__(self):
        return f"{self.id}-{self.state}"

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
