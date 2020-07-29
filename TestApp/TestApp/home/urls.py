from django.urls import path
from . import views
from persons.views import TransactionView

urlpatterns = [
    path('', views.main, name='main'),
    path('new_transaction/', views.transactions, name='new_transaction'),
    path('admin', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('transaction/', TransactionView.as_view(), name='info'),
]
