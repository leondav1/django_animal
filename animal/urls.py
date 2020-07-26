from django.urls import path

from .views import AnimalsList, AnimalsCreate, AnimalDetail, AnimalsUpdate, AnimalsDelete

urlpatterns = [
    path('all/', AnimalsList.as_view(), name="animals-list"),
    path('animal/create/', AnimalsCreate.as_view(), name="create"),
    path('animal/<int:pk>/', AnimalDetail.as_view(), name="animal-detail-list"),
    path('animal/<int:pk>/delete/', AnimalsDelete.as_view(), name="animal-detail-list-delete"),
    path('animal/<int:pk>/update/', AnimalsUpdate.as_view(), name="animal-detail-list-update"),

]
