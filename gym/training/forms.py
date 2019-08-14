from django import forms
from training.models import GymExercise, CHOICES

from django.contrib.auth.models import User


class AddGymExerciseForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=255)
    description = forms.CharField(label="Opis", widget=forms.Textarea)
    type = forms.ChoiceField(label="Typ", widget=forms.Select, choices=CHOICES)

class AddMainPlanForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=255)
    description = forms.CharField(label="Opis", widget=forms.Textarea)
    user = forms.ModelChoiceField(label="Kursant", widget=forms.Select, queryset=User.objects.all())

class AddPartialPlanForm(forms.Form):
    name = forms.CharField(label="Nazwa Planu Cząstkowego", max_length=255)
    exercises = forms.ModelMultipleChoiceField(label="Ćwiczenia", widget=forms.CheckboxSelectMultiple, queryset=GymExercise.objects.all())


class AddWeekForm(forms.Form):
    name = forms.CharField(label="Tydzień", max_length=10)
    how_many_series = forms.IntegerField(label="Ile Serii")

class AddExercisesToPartialPlanForm(forms.Form):

    exercises = forms.ModelMultipleChoiceField(label="Ćwiczenia", widget=forms.CheckboxSelectMultiple, queryset=GymExercise.objects.all())


