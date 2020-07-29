from rest_framework import serializers
from .models import Transaction


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    balance = serializers.IntegerField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user_from', 'user_to', 'amount']
