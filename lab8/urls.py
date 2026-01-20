"""
URL configuration for lab8 project. 
(El resto de la descripción está bien)
"""
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from oauth2_provider import urls as oauth2_urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokedex.urls')) ,
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('o/', include((oauth2_urls, 'oauth2_provider'), namespace='oauth2_provider')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    