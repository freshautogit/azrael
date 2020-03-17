from django.urls import path, include
from django.views.generic.edit import FormView
from . import views


urlpatterns = [
	path('', views.indexYP, name='indexYP'),

	# Авторизированный поиск и добавление запси
	# в справочник со страницы авторизированного поиска
	path('search/', views.search, name='search'),
	path('search/adduser/', views.addUser, name='adduser'),

	# Добавить новую запись в справочник с главной страницы
	path('adduser/', views.addUser, name='adduser'),

	# Обычный поиск
	path('s/', views.regular_search, name='regular_search'),

	#Запросы с выпадающих списков
	path('s/test/', views.testHttpRequest, name='testHttpsRequest'),


	#############################################################
	# Добавить новую запись в справочник со страницы поиска
	# Удалить, изменить и сохранить запись в справочнике
	# со страницы обычного поиска
	path('s/adduser/', views.addUser, name='adduser'),
	path('s/deluser/', views.delUser, name='deluser'),
	path('s/edituser/', views.editUser, name='edituser'),
	path('s/saveuser/', views.saveUser, name='saveuser'),
	#############################################################

	path('test/', views.testHttpRequest, name='testHttpsRequest'),
	path('', include('django.contrib.auth.urls'))
]
