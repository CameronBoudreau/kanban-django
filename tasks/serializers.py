from rest_framework import serializers
from .models import Card

STATUS_CHOICES = ['Urgent', 'On Deck', 'In Progress', 'Complete']


class CardSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=20)
    description = serializers.CharField(required=True, allow_blank=True, style={'base_template': 'textarea.html'})
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default='On Deck')
    created = serializers.DateField()

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)

        instance.description = validated_data.get('description', instance.description)

        instance.status = validated_data.get('status', instance.status)

        instance.created = validated_data.get('created', instance.created)

        instance.save()
        return instance
