from  django import template
from news.models import CategoryDB, NewsDB

register = template.Library()


@register.simple_tag()
def get_categories():
    '''
    Симпл тег отдает запрошенные данные из БД, которые затем
    подключаются в нужном шаблоне, и далее обрабатываются.
    '''
    return CategoryDB.objects.all()


@register.inclusion_tag('news/_list_categories.html')
def show_categories():
    '''
    Инклюжен тег принимает указанный шаблон, рендерит его, включает
    необходимые данные из БД, и, соответственно, на выходе уже готовый продукт.
    '''
    categories = CategoryDB.objects.all()
    return {'categories': categories}
