from rest_framework import serializers

from apps.accounts.models import AppUser

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ["id", "email", "username", "role"]