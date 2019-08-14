from training.forms import AddGymExerciseForm, AddMainPlanForm, AddPartialPlanForm, AddWeekForm, AddExercisesToPartialPlanForm


from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from training.models import Series, Week, GymExercise, MainPlan, PartialPlan





class AddGymExerciseView(View):

    def get(self, request):
        form = AddGymExerciseForm

        return render(request, 'add_gym_exercise.html', {'form': form})

    def post(self, request):
        form = AddGymExerciseForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            type = form.cleaned_data['type']

            try:
                GymExercise.objects.create(name=name, description=description, type=type)
                return render(request, 'add_gym_exercise.html', {'form': form, 'message': 'Dodano nowe ćwiczenie'})
            except:
                return render(request, 'add_gym_exercise.html', {'form': form, 'message': 'Takie Ćwiczenie jest już w bazie'})

class AddMainPlanView(View):
    def get(self, request):
        form = AddMainPlanForm()

        return render(request, 'add_main_plan.html', {'form': form})

    def post(self, request):
        form = AddMainPlanForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            user = form.cleaned_data['user']
            main_plan = MainPlan.objects.create(name=name, description=description, user_id=user.id)
            return render(request, 'add_main_plan.html', {'form': form, 'main_plan':main_plan})

class AddPartialPlanView(View):
    def get(self, request, id):


        if id:
            main_plan = MainPlan.objects.get(id=id)
            form = AddPartialPlanForm
            return render(request, 'add_partial_plan.html', {'form': form, 'id':main_plan.id})
        else:
            return HttpResponseRedirect('/add_main_plan/')

    def post(self, request, id):


        form = AddPartialPlanForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            main_plan = MainPlan.objects.get(id=id)
            # main_plan = form.cleaned_data['main_plan']
            exercises = form.cleaned_data['exercises']

            new_partial_plan = PartialPlan.objects.create(name=name, main_plan=main_plan)

            for exercise in exercises:
                new_partial_plan.exercises.add(exercise)

            return render(request, 'add_partial_plan.html', {'form': form, 'id':main_plan.id})

class ShowPartialPlanView(View):
    def get(self, request, id):

        partial_plan = PartialPlan.objects.get(id=id)

        return render(request, 'show_partial_plan.html', {'partial_plan': partial_plan})

    def post(self, request, id):

        partial_plan = PartialPlan.objects.get(id=id)
        exercise_id = request.POST.get('Delete')
        if exercise_id:

            partial_plan.exercises.remove(GymExercise.objects.get(id=exercise_id))
            partial_plan.save()



        return render(request, 'show_partial_plan.html', {'partial_plan': partial_plan})

class AddExercisesToPartialPlanView(View):
    def get(self, request, id):

        form = AddExercisesToPartialPlanForm

        return render(request, 'add_exercises_to_partial_plan.html', {'form': form, 'id':id})

    def post(self, request, id):

        form = AddExercisesToPartialPlanForm(request.POST)
        partial_plan = PartialPlan.objects.get(id=id)

        if form.is_valid():
            exercises = form.cleaned_data['exercises']

            for exercise in exercises:
                partial_plan.exercises.add(exercise)
            partial_plan.save()


        return render(request, 'add_exercises_to_partial_plan.html', {'form': form, 'id':id})



class AddWeekView(View):
    def get(self, request, plan_id, exercise_id, partial_plan_id):


        form = AddWeekForm()

        main_plan = MainPlan.objects.get(id=plan_id)
        exercise = GymExercise.objects.get(id=exercise_id)
        partial_plan = PartialPlan.objects.get(id=partial_plan_id)


        return render(request, 'add_week.html', {'form': form, 'exercise_id':exercise_id, 'plan_id':plan_id, 'partial_plan_id':partial_plan_id, "range":range(10),
                                                'main_plan':main_plan, 'exercise':exercise, 'partial_plan':partial_plan})

    def post(self, request, plan_id, exercise_id, partial_plan_id):


        form = AddWeekForm(request.POST)


        if form.is_valid():
            name = form.cleaned_data['name']
            how_many_series = form.cleaned_data['how_many_series']

            rep1 = request.POST.get('1')
            rep2 = request.POST.get('2')
            rep3 = request.POST.get('3')
            rep4 = request.POST.get('4')
            rep5 = request.POST.get('5')
            rep6 = request.POST.get('6')
            rep7 = request.POST.get('7')
            rep8 = request.POST.get('8')
            rep9 = request.POST.get('9')
            rep0 = request.POST.get('0')

            load1 = request.POST.get('second1')
            load2 = request.POST.get('second2')
            load3 = request.POST.get('second3')
            load4 = request.POST.get('second4')
            load5 = request.POST.get('second5')
            load6 = request.POST.get('second6')
            load7 = request.POST.get('second7')
            load8 = request.POST.get('second8')
            load9 = request.POST.get('second9')
            load0 = request.POST.get('second0')

            week = Week.objects.create(name=name, how_many_series=how_many_series, exercise_id=exercise_id, partial_plan_id=partial_plan_id)

            if rep1 and load1:
                Series.objects.create(reps=rep1, load=load1, week_id=week.id)
            else:
                pass

            if rep2 and load2:
                Series.objects.create(reps=rep2, load=load2, week_id=week.id)
            else:
                pass

            if rep3 and load3:
                Series.objects.create(reps=rep3, load=load3, week_id=week.id)
            else:
                pass

            if rep4 and load4:
                Series.objects.create(reps=rep4, load=load4, week_id=week.id)
            else:
                pass

            if rep5 and load5:
                Series.objects.create(reps=rep5, load=load5, week_id=week.id)
            else:
                pass

            if rep6 and load6:
                Series.objects.create(reps=rep6, load=load6, week_id=week.id)
            else:
                pass

            if rep7 and load7:
                Series.objects.create(reps=rep7, load=load7, week_id=week.id)
            else:
                pass

            if rep8 and load8:
                Series.objects.create(reps=rep8, load=load8, week_id=week.id)
            else:
                pass

            if rep9 and load9:
                Series.objects.create(reps=rep9, load=load9, week_id=week.id)
            else:
                pass

            if rep0 and load0:
                Series.objects.create(reps=rep0, load=load0, week_id=week.id)
            else:
                pass


            return HttpResponseRedirect(f'/show_plan/{plan_id}/')


class ShowMainPlanView(View):
    def get(self, request, id):

        plan = MainPlan.objects.get(id=id)
        partial_plans = PartialPlan.objects.filter(main_plan_id=plan.id)

        weeks = Week.objects.all()
        series = Series.objects.all()
        context = {"plan":plan, "partial_plans": partial_plans, "weeks": weeks, "series":series}

        return render(request, 'show_plan.html', context)

    def post(self, request, id):

        partial_plan_id = request.POST.get('Delete')

        if partial_plan_id:
            PartialPlan.objects.get(id=partial_plan_id).delete()

        plan = MainPlan.objects.get(id=id)
        partial_plans = PartialPlan.objects.filter(main_plan_id=plan.id)
        weeks = Week.objects.all()
        series = Series.objects.all()
        context = {"plan": plan, "partial_plans": partial_plans, "weeks": weeks, "series": series}

        return render(request, 'show_plan.html', context)


class ShowAllPlansView(View):
    def get(self, request):

        main_plans = MainPlan.objects.all()

        return render(request, 'show_all_plans.html', {'main_plans': main_plans})

    def post(self, request):

        main_plan_id = request.POST.get('Delete')
        main_plan = MainPlan.objects.get(id=main_plan_id)

        if main_plan_id:
            main_plan.delete()


        main_plans = MainPlan.objects.all()

        return render(request, 'show_all_plans.html', {'main_plans': main_plans})

class ShowAllGymExercisesView(View):
    def get(self, request):

        gym_exercises = GymExercise.objects.all()

        return render(request, 'show_all_exercises.html', {'gym_exercises': gym_exercises})

    def post(self, request):

        exercise_id = request.POST.get('Delete')
        gym_exercise = GymExercise.objects.get(id=exercise_id)

        if exercise_id:
            gym_exercise.delete()

        gym_exercises = GymExercise.objects.all()

        return render(request, 'show_all_exercises.html', {'gym_exercises': gym_exercises})












