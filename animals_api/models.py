from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Animal(models.Model):
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    nickname = models.CharField(verbose_name="Кличка", max_length=120)
    age = models.IntegerField(verbose_name="Возраст")
    arrival_date = models.DateField(verbose_name="Дата прибытия")
    weight = models.FloatField(verbose_name="Вес")
    growth = models.FloatField(verbose_name="Рост")
    special_signs = models.CharField(verbose_name="Особые приметы", max_length=300)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Список животных'
