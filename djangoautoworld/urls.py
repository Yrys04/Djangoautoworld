"""
URL configuration for djangoautoworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from cars import views
  
urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact_ajax, name='contact'),
    path("success/", views.success_page, name='success_page'),
    path('admin/', admin.site.urls),
    path("catalog/new/", views.new_cars, name='new_cars'),
    path("catalog/used/", views.used_cars, name='used_cars'),
    path("catalog/promo/", views.promo_cars, name='promo_cars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)