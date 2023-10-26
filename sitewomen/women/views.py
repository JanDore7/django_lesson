from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти',]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'ГЛАВНАЯ СТРАНИЦА',
            'menu': menu,
            'float': 22.01,
            'lst': [1, 'abc', True],
            'set': {1, 2, 3, 4},
            'dict': {'key1': 'value1', 'key2': 'value2'},
            'obj': MyClass(10, 20),
            'url': slugify('The may page')
            }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О САЙТЕ'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>категория: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>год: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')