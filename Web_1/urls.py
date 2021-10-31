
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    re_path(r'^products/(?P<productid>\d+)/', views.products, name='products'),
    path('', views.index, name='home'),
    re_path(r'^about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),

]
