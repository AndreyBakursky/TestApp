from django.urls import path, re_path
from .views import UserView, TransactionView


app_name = "users"


urlpatterns = [
        path('users/', UserView.as_view()),
        path('transaction/', TransactionView.as_view(),
        name='transfer')
]
