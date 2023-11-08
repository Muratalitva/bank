from django.db import models
from apps.users.models import BankUser
# Create your models here.

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        BankUser,
        on_delete=models.CASCADE,
        related_name='from_user',
        verbose_name='От пользователя'
    )
    to_user = models.ForeignKey(
        BankUser,
        on_delete=models.CASCADE,
        related_name='to_user',
        verbose_name='Пользователю'
    )
    is_complated = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    amount = models.CharField(
        max_length=255,
        verbose_name='Количество'
    )

    def __str__(self):
        return self.amout
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'