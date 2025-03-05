from rest_framework import serializers
from .models import Memory

from django.contrib.auth.models import User


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ["id", "title", "description", "published_at", "owner"]
        owner = serializers.ReadOnlyField(source="owner.username")


class UserSerializer(serializers.ModelSerializer):
    memories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Memory.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "memories"]
