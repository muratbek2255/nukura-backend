from datetime import datetime

from django.db import models

from apirest.managers import CommentManager
from nukura.models import NukuraStore
from users.models import CustomUser


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Имя", max_length=100)
    message = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    nukura = models.ForeignKey(NukuraStore, verbose_name="отзывы", on_delete=models.CASCADE)

    objects = CommentManager()

    def __str__(self):
        return f"{self.name} - {self.nukura}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"