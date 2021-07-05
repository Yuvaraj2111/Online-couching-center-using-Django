"""adproject URL Configuration
	
	for app

"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('index/<str:i>/',views.home,name="home"),
    path('about/<str:j>/',views.about,name="about"),
    path('contact/<str:i>/', views.contact, name="contact"),
    path('admission/<str:i>/', views.admission, name="admission"),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('enroll/<str:i>/<str:j>/', views.enroll, name="enroll"),
    path('course/<str:i>/', views.course, name="course"),
    path('course_single/<str:i>/<str:j>/', views.cs, name="course_single"),
    path('logout/', views.logout, name="logout"),
  ]
