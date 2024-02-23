# api/views.py
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer