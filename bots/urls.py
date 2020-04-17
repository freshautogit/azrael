from django.urls import path
from . import views


urlpatterns = [
	path('aster_create_task/', views.aster_create_task, name='aster_create_task'),
	path('bi/', views.bi, name='bi')
]
