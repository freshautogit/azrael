from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('yellowpages.urls')),
    path('admin/', admin.site.urls),
]