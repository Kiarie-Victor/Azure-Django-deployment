"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from project import settings
from ms_identity_web.django.msal_views_and_urls import MsalViews
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('', include('dog_shelters.urls')),
    path('admin/', admin.site.urls),
    path(f'{settings.AADConfig.django.auth_endpoints.prefix}/', include(msal_urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
