from django.db import models
from decimal import Decimal
import uuid

class User(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=16,
    max_digits=32)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    user_from = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='transactions_by_user_from'
    )

    user_to = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='transactions_by_user_to'
    )

    amount = models.DecimalField(decimal_places=16,
    max_digits=32)

    created_at = models.DateTimeField(auto_now_add=True,
    db_index=True)
