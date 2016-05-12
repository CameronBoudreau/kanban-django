from rest_framework import viewsets
from .models import Cards
from .serializers import CardsSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all().order_by('status')
    serializer_class = CardsSerializer
