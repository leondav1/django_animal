from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from animals_api import models
from animals_api.models import Animal
from animals_api.serializers import AnimalListSerializer, AnimalDetailSerializer
from .forms import AnimalForm


class AnimalsList(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.has_perm('animals_api.view_animal'):
            animals = Animal.objects.all()
            serializer = AnimalListSerializer(animals, many=True)
            data = {'data': serializer.data}
            return render(request=request, template_name='animal/list.html', context=data)
        raise PermissionDenied


class AnimalsCreate(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.has_perm('animals_api.add_animal'):
            form = AnimalForm()
            return render(request=request, template_name='animal/create.html', context={'form': form})
        return redirect(reverse('animals-list'))

    def post(self, request):
        bound_form = AnimalForm(request.POST)
        print(bound_form)
        if bound_form.is_valid():
            new_animal = bound_form.save(commit=False)
            new_animal.user = request.user
            new_animal.save()
            return redirect(reverse('animals-list'))


class AnimalDetail(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.has_perm('animals_api.view_animal'):
            animal = Animal.objects.get(id=kwargs['pk'])
            serializer = AnimalDetailSerializer(animal)
            return render(request=request, template_name='animal/detail.html', context={'data': serializer.data})
        raise PermissionDenied


class AnimalsUpdate(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.has_perm('animals_api.change_animal'):
            item = get_object_or_404(models.Animal, id=kwargs['pk'])
            form = AnimalForm(request.POST or None, instance=item)
            return render(request=request, template_name='animal/update.html', context={'form': form, 'id': kwargs['pk']})
        return redirect(reverse('animals-list'))

    def post(self, request, *args, **kwargs):
        animal = Animal.objects.get(id=kwargs['pk'])
        bound_form = AnimalForm(request.POST, instance=animal)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse('animals-list'))


class AnimalsDelete(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if request.user.has_perm('animals_api.delete_animal'):
            animal = Animal.objects.get(id=kwargs['pk'])
            serializer = AnimalDetailSerializer(animal)
            return render(request=request, template_name='animal/delete.html', context={'data': serializer.data})
        return redirect(reverse('animals-list'))

    def post(self, request, *args, **kwargs):
        animal = Animal.objects.get(id=kwargs['pk'])
        animal.delete()
        return redirect(reverse('animals-list'))
