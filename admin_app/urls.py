"""adproject URL Configuration
	
	for app

"""

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="ad"),
    path('add_admin/',views.add,name="add_admin"),
    path('add_home/<str:i>/',views.adminhome,name="add_home"),
    path('delete/<str:j>/',views.admin_del,name="add_del"),
    # path('add_student/',views.student, name="student")

    # path('',views.add,name="add_home"),
  ]

