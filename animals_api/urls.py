from django.urls import path, include

from .views import AnimalCreateView, AnimalsListView, AnimalDetailView

urlpatterns = [
    path('animal/create/', AnimalCreateView.as_view()),
    path('all/', AnimalsListView.as_view()),
    path('animal/detail/<int:pk>/', AnimalDetailView.as_view()),
]
