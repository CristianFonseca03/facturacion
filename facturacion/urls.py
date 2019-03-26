"""facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from facturacion.views import HomeView, PersonDetail, DeletePersona, CreatePersona, CreateProductos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', PersonDetail.as_view(), name='detail'),
    path('delete/<int:pk>', DeletePersona.as_view(), name='delete'),
    path('create/', CreatePersona.as_view(), name='createPerson'),
    path('create/product/', CreateProductos.as_view(), name='createProduct'),
]
