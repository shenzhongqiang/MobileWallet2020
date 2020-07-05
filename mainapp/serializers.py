from .models import User, Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    from_user = serializers.ReadOnlyField(source='from_user.username')
    to_user = serializers.ReadOnlyField(source='to_user.username')

    class Meta:
        model = Transaction
        fields = ['id', 'from_user', 'to_user', 'amount', 'timestamp']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    my_sent = TransactionSerializer(many=True)
    my_received = TransactionSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'balance', 'my_sent', 'my_received']

