
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('menu/', include("menu.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  staticfiles_urlpatterns()
