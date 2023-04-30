from main.models import UserKeys
from rest_framework import serializers


class UserKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKeys
        fields = ['id', 'user', 'mnemonic']
