
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
