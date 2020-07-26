from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from .models import Animal
from .serializers import AnimalDetailSerializer, AnimalListSerializer
from .permissions import IsOwnerOrReadOnly


class AnimalCreateView(generics.CreateAPIView):
    serializer_class = AnimalDetailSerializer


class AnimalsListView(generics.ListAPIView):
    serializer_class = AnimalListSerializer
    queryset = Animal.objects.all()
    permission_classes = (IsAuthenticated, )


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalDetailSerializer
    queryset = Animal.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser, )

