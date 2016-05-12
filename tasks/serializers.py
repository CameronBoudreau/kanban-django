from rest_framework import serializers
from .models import Cards


class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ('url', 'title', 'description', 'status')
