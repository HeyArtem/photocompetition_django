from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from conf.settings import django

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('photo_competition.urls')),
              ] + static(django.MEDIA_URL, document_root=django.MEDIA_ROOT)

urlpatterns += static(django.STATIC_URL, document_root=django.STATIC_ROOT)
