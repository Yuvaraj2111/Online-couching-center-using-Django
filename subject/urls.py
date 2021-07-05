"""adproject URL Configuration
	
	for app

"""

from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add_subject/',views.add_subject,name="add_subject"),
    path('dis/', views.display, name="disp_video"),
    # path('add_student/',views.student, name="student")

    # path('',views.add,name="add_home"),
  ]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   