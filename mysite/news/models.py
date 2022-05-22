from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey



class NewsDB(models.Model):
    """Класс таблицы списка новостей в БД"""
    title = models.CharField(max_length=150, verbose_name='Наименование новости')
    content = models.TextField(blank=True, verbose_name='Контент')  # blank=True - указывает, что поле не является обязательным к заполнению
    date_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')   # auto_now_add=True - указываем, что поле заполнится 1 раз, при создании, и в дальнейшем меняться не будет
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')    # auto_now=True - значение поля будет обновляться каждый раз при редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)  # upload_to='photos/%Y/%m/%d' - указываем путь, куда будут сохраняться фотки, причем с созданием структуры подпапок по дате
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')    # default=True - по умолчанию ставим True - т.е. публикуем новость
    category = models.ForeignKey('CategoryDB', on_delete=models.PROTECT, null=True, verbose_name='Категория')    # первый параметр - название модели, при этом мы можем передавать его в 2 видах: либо ссылка на модель, либо строка с именем модели. models.PROTECT обеспечивает защиту от удаления данных

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        """Форматирование данных, выводимых админу"""
        verbose_name = 'Новость'    # наименование модели в единственном числе
        verbose_name_plural = 'Новости'    # наименование модели во множественном числе
        ordering = ['-date_at'] # указываем сортировку списка новостей, которая будет выводиться админу
        # также, указанный здесь порядок сортировки будет влиять на порядок сортировки списка новостей, выводимых пользователю


class CategoryDB(models.Model):
    """Класс таблицы категорий новостей в БД"""
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')     # db_index=True - Если True, для этого поля будет создан индекс базы данных, т.е. поле индексируется, что делает его более быстрым для поиска

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        """Форматирование данных, выводимых админу"""
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
