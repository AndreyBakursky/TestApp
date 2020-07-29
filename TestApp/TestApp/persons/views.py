from decimal import Decimal


from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.transaction import atomic

from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': users})


    def post(self, request):
        persons = request.data.get('persons')
        serializer = UserSerializer(data=persons)
        if serializer.is_valid(raise_exception=True):
            persons_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(persons_saved.title)})

class TransactionView(APIView):

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        with atomic():
            amount = Decimal(serializer.validated_data["amount"])

            user_from = User.objects.filter(pk=serializer.validated_data["user_from"].id).select_for_update().first()

            user_to = User.objects.filter(pk=serializer.validated_data["user_to"].id).select_for_update().first()

            if user_from.balance - amount < Decimal("0"):
                return Response({"status": "ERROR", "error": f"user {serializer.validated_data['user_from']} has not enought funds"})


            new_transaction = serializer.save()

            user_from.balance -= new_transaction.amount
            user_from.save(update_fields=['balance'])

            user_to.balance += new_transaction.amount
            user_to.save(update_fields=['balance'])

        return Response({"status": "OK", "data": {"uuid": new_transaction.uuid}})
