from django.urls import path
from . import views


urlpatterns = [
	path('aster_create_task/', views.aster_create_task, name='aster_create_task'),
	path('bi/', views.bi, name='bi'),
	path('zabbix_create_task/', views.zabbix_create_task, name='zabbix_create_task')
]
