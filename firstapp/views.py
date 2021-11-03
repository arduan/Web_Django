from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


# def index(request):
#      header = 'Персональные данные'
#      langs = ['Английский', 'Немецкий', 'Испанский']
#      user = {'name': 'Виталий', 'age': 62}
#      address = ('Ленина', 117, 119)
#      data = {'header': header, 'user': user, 'langs': langs, 'address': address}
#      return render(request, 'index.html', context=data)

def index(request):
    data = ['Ноутбуки', 'Принтеры', 'Сканеры', 'Диски', 'Шнуры']
    return render(request, 'firstapp/index.html', context={'data': data})


def about(request):
    return HttpResponse('<h3>О сайте</h3>')


def contact(request):
    return HttpResponseRedirect('/about')


def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)
