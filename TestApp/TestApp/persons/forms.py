from .models import Transaction
from django.forms import ModelForm, TextInput


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount"]
        widgets = {
            "amount": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите сумму'
            })
        }
