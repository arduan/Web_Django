
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    # Параметры функции path () заключаются в угловые скобки в формате:
    # <спецификатор:наэвание_параметра>
    path('products/<int:productid>/', views.products, name='products'),
    path('products/', views.products),
    path('', views.index, name='home'),
    re_path(r'^about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),

]
