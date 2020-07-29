from persons.models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "balance"]
        widgets = {
            "name": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите имя пользователя'
            }),
            "balance": TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Введите начальный баланс'
            })
}
