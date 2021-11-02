
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from firstapp import views

urlpatterns = [
    path('products/<int:productid>/', views.products, name='products'),
    path('products/', views.products),
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='firstapp/about.html')),
    path('contact/', TemplateView.as_view(template_name='firstapp/contact.html')),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),

]
