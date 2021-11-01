from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    # return render(request, 'firstapp/home.html')
    data = {'header':'Передача параметров в шаблон Django', 'message': 'Загружен шаблон  templates/firstapp/index_app.html'}
    return render(request, 'firstapp/index_app1.html', context=data)

def about(request):
    return HttpResponse('<h3>О сайте</h3>')


def contact(request):
    return HttpResponseRedirect('/about')


def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категория: {1}</h2>'.format(productid, category)
    return HttpResponse(output)
