

from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('enr/<str:a>/',views.show,name="show"),
    path('learn/<str:i>/<str:j>/', views.display, name="learn"),
    path('certificate/<str:i>/<str:j>/',views.certificate, name="certificate"),

    ]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   