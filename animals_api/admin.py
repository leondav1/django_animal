from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'age', 'arrival_date', 'weight', 'growth', 'special_signs')
    list_filter = ['nickname', 'age', 'weight', ]
    search_fields = ['id', 'nickname', ]
    actions_on_top = True
    actions_on_bottom = False
