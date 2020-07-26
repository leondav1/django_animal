from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Animal


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        # exclude = []
        fields = "__all__"


class AnimalDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Animal
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

