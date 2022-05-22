from django.contrib import admin
from .models import NewsDB, CategoryDB


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_at', 'updated_at', 'is_published', 'category')  # именно эти поля будут выводиться админу в списке новостей
    list_display_links = ('id', 'title')  # именно эти поля в списке новостей админа будут ссылками
    search_fields = ('title', 'content')  # поля, по которым будет производиться поиск, собственно, именно после введения этой переменной появится поле поиска у админа
    list_editable = ('is_published',)    # указываем, что это поле мы хотим редактировать прямо из списка
    list_filter = ('is_published', 'category')  # указываем, по каким полям мы хотим фильтровать новости


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # здесь нужно указывать кортеж, соответственно, если элемент 1, ставим после него запятую, иначе будет интерпретация, что это строка


admin.site.register(NewsDB, NewsAdmin)  # сначала мы регистрируем саму модель, а затем уже класс, который ее настроит
admin.site.register(CategoryDB, CategoryAdmin)
