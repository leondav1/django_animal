from django import forms
from animals_api.models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nickname', 'age', 'arrival_date', 'weight', 'growth', 'special_signs', ]
    # nickname = forms.CharField(max_length=120)
    # age = forms.IntegerField()
    # arrival_date = forms.DateField()
    # weight = forms.FloatField()
    # growth = forms.FloatField()
    # special_signs = forms.CharField(max_length=300)

    # def save(self):
    #     new_animal = Animal.objects.create(
    #         nickname=self.cleaned_data['nickname'],
    #         age=self.cleaned_data['age'],
    #         arrival_date=self.cleaned_data['arrival_date'],
    #         weight=self.cleaned_data['weight'],
    #         growth=self.cleaned_data['growth'],
    #         special_signs=self.cleaned_data['special_signs']
    #     )
    #     return new_animal
