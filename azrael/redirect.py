from django.contrib import admin
from django.urls import path, include
import yellowpages
urlpatterns = [
    path('', yellowpages.views.redirect_to_help),
]