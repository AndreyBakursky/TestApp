from django.db import models


class Clients(models.Model):
    vladelets = models.TextField(max_length=60)
    schet = models.PositiveIntegerField(null=False)
    balance = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.vladelets


    class Meta:
        verbose_name = 'Клиент ТестБанка'
        verbose_name_plural = 'Клиенты ТестБанка'
