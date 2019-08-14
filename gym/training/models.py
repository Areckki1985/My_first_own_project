from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    (1, "Główne"),
    (2, "Akcesoryjne"),
    (3, "Korekcyjne"),
)

DAY_NAMES = (
    (1, "Poniedziałek"),
    (2, "Wtorek"),
    (3, "Środa"),
    (4, "Czwartek"),
    (5, "Piątek"),
    (6, "Sobota"),
    (7, "Niedziela"),

)
class Series(models.Model):
    reps = models.IntegerField(null=True)
    load = models.IntegerField(null=True)
    week = models.ForeignKey('Week', on_delete=models.CASCADE)

class Week(models.Model):
    name = models.CharField(max_length=10)
    how_many_series = models.IntegerField(null=True)
    exercise = models.ForeignKey('GymExercise', on_delete=models.CASCADE)
    partial_plan = models.ForeignKey('PartialPlan', on_delete=models.CASCADE)

class GymExercise(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    type = models.CharField(max_length=1, choices=CHOICES, default=1)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    movie_link = models.TextField(null=True)

    def __str__(self):
        return self.name

class MainPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PartialPlan(models.Model):
    name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(GymExercise)
    main_plan = models.ForeignKey(MainPlan, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_coach = models.BooleanField(default=True)










