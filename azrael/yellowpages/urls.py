from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_yp, name='index_yp'),

    # Авторизированный поиск и добавление запси
    # в справочник со страницы авторизированного поиска
    path('search/', views.search, name='search'),
    path('addinfo/', views.add_info, name='add_info'),
    path('search/adduser/', views.add_user, name='add_user'),
    path('search/edituser/', views.edit_user, name='edit_user'),
    path('search/saveuser/', views.save_user, name='save_user'),
    path('search/deluser/', views.del_user, name='del_user'),
    path('search/adduser/dropdown_request/', views.dropdown_request, name='dropdown_request'),

    # Добавить новую запись в справочник с главной страницы
    path('adduser/', views.add_user, name='add_user'),

    # Обычный поиск
    path('s/', views.regular_search, name='regular_search'),

    # Запросы с выпадающих списков
    path('s/dropdown_request/', views.dropdown_request, name='dropdown_request'),

    #############################################################
    # Добавить новую запись в справочник со страницы поиска
    # Удалить, изменить и сохранить запись в справочнике
    # со страницы обычного поиска
    path('s/adduser/', views.add_user, name='add_user'),
    path('s/deluser/', views.del_user, name='del_user'),
    path('s/edituser/', views.edit_user, name='edit_user'),
    path('s/saveuser/', views.save_user, name='save_user'),
    #############################################################

    path('dropdown_request/', views.dropdown_request, name='dropdown_request'),
    path('', include('django.contrib.auth.urls'))
]
