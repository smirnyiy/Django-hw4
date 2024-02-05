from django.contrib import admin
from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls')),
    path('', index),
    path('les4/', include('myapp.urls')),
]
