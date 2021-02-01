from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index_yp, name='index_yp'),

    path('rateus/', views.form, name='form'),
    path('rateus/rating/', views.get_results, name="get_results"),

    path('search/', views.search, name='search'),
    path('search/edituser/', views.edit_user, name='edit_user'),
    path('search/edituser/deluser/', views.del_user, name='del_user'),

    path('s/', views.regular_search, name='regular_search'),
    path('s/dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('adduser/dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('addinfo/dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('edituser/dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('search/edituser/dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('search/dropdown_request/', views.dropdown_request, name='dropdown_request'),

    path('adduser/', views.add_user, name='add_user'),
    path('addinfo/', views.add_info, name='add_info'),
    path('saveuser/', views.save_user, name='save_user'),
    path('help/', include('helpapp.urls')),

    path('bots/', include('bots.urls')),
    path('', include('django.contrib.auth.urls')),
    path('reg/', views.regitstration, name="registration"),
]
