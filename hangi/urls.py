"""
URL configuration for hangi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

              ] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
    path('Gallery/', include('Gallery.urls')),
    path('our_team/', include('our_team.urls')),
    path('what_we_do/', include('what_we_do.urls')),
    path('what_we_doing/', include('what_we_doing.urls', namespace='what_we_doing')),
    path('', include('main.urls')),
    path('phartner/', include('phartner.urls')),
    path('social/', include('social.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
