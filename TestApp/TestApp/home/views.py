from django.shortcuts import render, redirect
from .models import Clients
from .forms import UserForm
from persons.models import User
from persons.forms import TransactionForm



def main(request):
    clients_of_bank = User.objects.all()
    return render(request, 'persons/main.html', {'title': 'Клиенты ТестБанка', 'clients_of_bank': clients_of_bank})

def transactions(request):
    clients_of_bank = User.objects.all()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
    form = TransactionForm()
    new = {'form': form}
    return render(request, 'persons/transaction.html', {'clients_of_bank': clients_of_bank})

def sign_up(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверный тип данных'


    form = UserForm()
    newclient = {'form': form,
                 'error': error}
    return render(request, 'home/sign_up.html', newclient)

def log_in(request):
    return render(admin.site.urls)
