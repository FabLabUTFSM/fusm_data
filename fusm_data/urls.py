"""fusm_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from rest_framework_extensions.routers import ExtendedDefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from perfiles.routing import router as PerfilesRouter
from sistema.urls import router as UsuarioRouter
from maquinas.routing import router as MaquinasRouter

...

schema_view = get_schema_view(
   openapi.Info(
      title="FabLab UTFSM API",
      default_version='v1',
      description="Test description"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

default_router = ExtendedDefaultRouter()
default_router.registry.extend(PerfilesRouter.registry)
default_router.registry.extend(UsuarioRouter.registry)
default_router.registry.extend(MaquinasRouter.registry)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(default_router.urls))
]
