from django.urls import path

from . import views

app_name = 'mainApp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('<single_slug>', views.single_slug, name='single_slug'),
    path('addTutorial/', views.add_new_tutorial, name='addTutorial'),
    path('addCategory/', views.add_new_tutorial_category, name='addCategory'),
    path('addSeries/', views.add_new_tutorial_series, name='addSeries'),
]