from django.urls import path, include
from django.views.generic.edit import FormView
from . import views


urlpatterns = [
	path('', views.indexYP, name='indexYP'),
	path('search/', views.search, name='search'),
	path('s/adduser/', views.addUser, name='adduser'),
	path('search/adduser/', views.addUser, name='adduser'),
	path('adduser/', views.addUser, name='adduser'),
	path('s/deluser/', views.delUser, name='deluser'),
	path('s/edituser/', views.editUser, name='edituser'),
	path('s/saveuser/', views.saveUser, name='saveuser'),
	path('s/', views.regular_search, name='regular_search'),
	path('test/', views.testHttpRequest, name='testHttpsRequest'),
	path('s/test/', views.testHttpRequest, name='testHttpsRequest'),
	path('', include('django.contrib.auth.urls'))
]
