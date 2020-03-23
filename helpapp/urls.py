from django.urls import path
from django.views.generic.edit import FormView
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('wh/', views.webhook, name='webhook'),
	path('success/', views.success, name='success')
]