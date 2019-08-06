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
from django.urls import path
from django.conf.urls import url

from training.views import AddGymExerciseView, AddMainPlanView, AddPartialPlanView, ShowMainPlanView, AddWeekView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^add_exercise/', AddGymExerciseView.as_view()),
    url(r'^add_main_plan/', AddMainPlanView.as_view()),
    url(r'^add_partial_plan/', AddPartialPlanView.as_view()),
    url(r'^show_plan/(?P<id>(\d)+)/', ShowMainPlanView.as_view()),
    url(r'^add_week/(?P<plan_id>(\d)+)/(?P<exercise_id>(\d)+)/(?P<partial_plan_id>(\d)+)/', AddWeekView.as_view()),
]
