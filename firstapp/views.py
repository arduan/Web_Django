from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.http import *


# def index(request):
#      header = 'Персональные данные'
#      langs = ['Английский', 'Немецкий', 'Испанский']
#      user = {'name': 'Виталий', 'age': 62}
#      address = ('Ленина', 117, 119)
#      data = {'header': header, 'user': user, 'langs': langs, 'address': address}
#      return render(request, 'index.html', context=data)

def index(request):
    userform = UserForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        output = '<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>'.format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
    return render(request, 'firstapp/index1.html', {'form': userform})


def about(request):
    return HttpResponse('<h3>О сайте</h3>')


def contact(request):
    return HttpResponseRedirect('/about')


def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)
