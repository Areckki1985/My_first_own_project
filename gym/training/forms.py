from django import forms
from training.models import Series, Week, GymExercise, MainPlan, PartialPlan, CHOICES


class AddGymExerciseForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=255)
    description = forms.CharField(label="Opis", widget=forms.Textarea)
    type = forms.ChoiceField(label="Typ", widget=forms.Select, choices=CHOICES)

class AddMainPlanForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=255)
    description = forms.CharField(label="Opis", widget=forms.Textarea)

class AddPartialPlanForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=255)
    exercises = forms.ModelMultipleChoiceField(label="Ćwiczenia", widget=forms.CheckboxSelectMultiple, queryset=GymExercise.objects.all())
    main_plan = forms.ModelChoiceField(label="Plan", queryset=MainPlan.objects.all())

class AddWeekForm(forms.Form):
    name = forms.CharField(label="Tydzień", max_length=10)
    how_many_series = forms.IntegerField(label="Ile Serii")

# class AddSeriesForm(forms.Form):
#     reps = forms.IntegerField()
#     load = forms.IntegerField()

