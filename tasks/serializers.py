from rest_framework import serializers
from .models import Card
from django.contrib.auth.models import User

STATUS_CHOICES = ['Urgent', 'In Progress', 'Complete']


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Card
        fields = ('id', 'owner', 'title', 'description', 'status', 'created')


class UserSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Card.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'cards')
