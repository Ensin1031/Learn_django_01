from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import NewsDB, CategoryDB
from .forms import AddNewsForm


def index(request):
    '''главная страница'''
    news = NewsDB.objects.all()
    cont = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/boot_index.html', cont)
    # имеет 3 обязательных параметра: request, имя_шаблона, и словарь с данными, которые необходимо передать в шаблон


def get_category(request, category_id):
    '''функция страницы выборки по категориям'''
    news = NewsDB.objects.filter(category_id=category_id)
    category = CategoryDB.objects.get(pk=category_id)
    cont = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', cont)


def view_news(request, news_id):
    '''функция страницы просмотра новости'''
    # news_item = NewsDB.objects.get(pk=news_id)
    news_item = get_object_or_404(NewsDB, pk=news_id)   # при такой организации запроса, пользователю вылетит правильная ошибка 404
    cont = {
        'title': news_item.title,
        'news_item': news_item
    }
    return render(request, 'news/view_news.html', cont)


def add_news(request):
    '''
    Функция страницы добавления новости.
    Вариант с формой, связанной с моделью
    '''
    if request.method == 'POST':
        form = AddNewsForm(request.POST)    # связываем форму с данными
        if form.is_valid():     # проверяем, прошла ли форма валидацию
            form.save()
            return redirect('home')    # подключаемая функция, после всех действий, переводит на указанную страницу
            # return redirect(news)   # вариант с пересылом на страницу новости
    else:
        form = AddNewsForm()
    cont = {
        'title': 'Добавление новости',
        'form': form
    }
    return render(request, 'news/add_news.html', cont)



def add_news_no_models(request):
    '''
    Функция страницы добавления новости.
    Вариант формы, не связанной с моделью
    '''
    if request.method == 'POST':
        form = AddNewsForm(request.POST)    # связываем форму с данными
        if form.is_valid():     # проверяем, прошла ли форма валидацию
            # print(form.cleaned_data)    # .cleaned_data - метод, выводящий содержимое заполненной формы в виде словаря
            news = NewsDB.objects.create(**form.cleaned_data)
            return redirect('home')    # подключаемая функция, после всех действий, переводит на указанную страницу
            # return redirect(news)   # вариант с пересылом на страницу новости
    else:
        form = AddNewsForm()
    cont = {
        'title': 'Добавление новости',
        'form': form
    }
    return render(request, 'news/add_news.html', cont)


def list_news(request):
    # так будет выглядеть функция без использования шаблона
    news = NewsDB.objects.all()
    res = '<h1>Список новостей</h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def test(request):
    print(request)
    return HttpResponse('<h1>Тестовая страница</h1>')
