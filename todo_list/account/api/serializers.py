from loguru import logger
from rest_framework import serializers

from account.models import Profile, Task
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['telegram_id']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class TaskSerializer(serializers.ModelSerializer):
    telegram_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ['telegram_id', 'title', 'description', 'completed']

    def create(self, validated_data):
        telegram_id = validated_data.pop('telegram_id')
        user = User.objects.get(profile__telegram_id=telegram_id)
        task = Task.objects.create(user=user, **validated_data)
        return task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        logger.warning('Serializer')