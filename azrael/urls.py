from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('wh/', include('helpapp.urls')),
    # path('help/', include('helpapp.urls')),
    # path('account/', include('yellowpages.urls')),
    path('admin/', admin.site.urls),
    # path('bots/', include('bots.urls')),
    # path('yp/', include('yellowpages.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('', include('yellowpages.urls')),
]
