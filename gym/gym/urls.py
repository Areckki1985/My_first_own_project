"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView

from training.views import AddGymExerciseView, AddMainPlanView, AddPartialPlanView, ShowMainPlanView, \
    AddWeekView, ShowAllPlansView, ShowPartialPlanView, AddExercisesToPartialPlanView, ShowAllGymExercisesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^add_exercise/', AddGymExerciseView.as_view()),
    url(r'^add_main_plan/', AddMainPlanView.as_view()),
    url(r'^add_partial_plan/(?P<id>(\d)+)/', AddPartialPlanView.as_view()),
    url(r'^show_plan/(?P<id>(\d)+)/', ShowMainPlanView.as_view()),
    url(r'^show_partial_plan/(?P<id>(\d)+)/', ShowPartialPlanView.as_view()),
    url(r'^add_week/(?P<plan_id>(\d)+)/(?P<exercise_id>(\d)+)/(?P<partial_plan_id>(\d)+)/', AddWeekView.as_view()),
    url(r'^show_all_plans/', ShowAllPlansView.as_view()),
    url(r'^show_all_exercises/', ShowAllGymExercisesView.as_view()),
    url(r'^add_exercises_partial_plan/(?P<id>(\d)+)/', AddExercisesToPartialPlanView.as_view()),



]
