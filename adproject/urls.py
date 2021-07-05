"""adproject URL Configuration


"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('myadmin/',include('admin_app.urls')),
    path('subject/',include('subject.urls')),
    path('courses/',include('course.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   