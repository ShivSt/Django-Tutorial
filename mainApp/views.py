from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import  TutorialForm, TutorialCategoryForm, TutorialSeriesForm
from django.contrib import messages
# Create your views here.
#A view function for a page
"""
def homepage(request):
    return HttpResponse('Hello you have started <strong>learning</strong> django framwork!!')
"""
#def single_slug()
def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request=request,
                      template_name='mainApp/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug = single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series = 
                                                this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_index = list(tutorials_from_series).index(this_tutorial)

        return render(request,
                      template_name="mainApp/tutorial.html",
                      context={"tutorial":this_tutorial,
                               "sidebar": tutorials_from_series,
                               "this_tut_idx": this_tutorial_index}
        )

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")




def homepage(request):
    return render(request=request,
                template_name="mainApp/home.html",
                context={"categories": TutorialCategory.objects.all})


def add_new_tutorial(request):

    if request.method == "POST":
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save()
            messages.info(request, f"Your tutorial #{tutorial.tutorial_title} is added")
            return redirect("mainApp:homepage")
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}: {form.errors[msg]}")

    form = TutorialForm
    return render(request=request,
                template_name="mainApp/inputForms/addTutorial.html",
                context={"form": form }) 


def add_new_tutorial_category(request):

    if request.method == "POST":
        form = TutorialCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Your tutorial Category is added")
            return redirect("mainApp:homepage")
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}: {form.errors[msg]}")

    form = TutorialCategoryForm
    return render(request=request,
                template_name="mainApp/inputForms/addCategory.html",
                context={"form": form }) 


def add_new_tutorial_series(request):

    if request.method == "POST":
        form = TutorialSeriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Your tutorial series is added")
            return redirect("mainApp:homepage")
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}: {form.errors[msg]}")

    form = TutorialSeriesForm
    return render(request=request,
                template_name="mainApp/inputForms/addSeries.html",
                context={"form": form }) 


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Accoutn created successfully: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("mainApp:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    form = UserCreationForm
    return render(request=request,
                template_name="mainApp/register.html",
                context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("mainApp:homepage")


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("mainApp:homepage")
            else:
                messages.error(request, f"Try again with a valid user credentials")
        else:
                messages.error(request, f"Try again with a valid user credentials")

    form = AuthenticationForm()
    return render(request=request,
                template_name="mainApp/login.html",
                context={"form":form})
    