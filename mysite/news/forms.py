from django import forms
from .models import CategoryDB, NewsDB
import re   # библиотека для работы с регулярными выражениями
from django.core.exceptions import ValidationError      # подключаем использование исключения


class AddNewsForm(forms.ModelForm):
    """Форма, связанная с моделью"""
    class Meta:     # подкласс, в котором и будет описание, как должна выглядеть наша форма
        model = NewsDB      # указываем, с какой моделью будет связанна наша форма
        # fields = '__all__'    #  в таком случае, в форме будут представлены все поля модели, не рекомендуется так делать
        '''здесь мы перечисляем поля модели, которые хотим видеть в нашей форме:'''
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {     # устанавливаем параметры на вывод полей формы
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):   # ищет цифры в title, если найдет - мы должны получить исключение ValidationError
            raise ValidationError('Название не должно начинаться с цифры.')
        return title


class AddNewsForm_no_worked(forms.Form):
    """Форма, не связанная с моделью"""
    title = forms.CharField(
        max_length=150,
        label='Название новой новости',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Текст новости',
        required=False,     # указываем, что заполнение данного поля не является обязательным
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5
        })
    )
    is_published = forms.BooleanField(
        label='Опубликовано',
        initial=True,   # указываем, что, по умолчанию, данный чек-бокс будет отмечен
    )
    category = forms.ModelChoiceField(
        empty_label='Выберите категорию',   # в данном поле указывается, чем заполнять не выбранное поле выпадающего списка. При установке значения None - по умолчанию будет стоять первое значение списка
        queryset=CategoryDB.objects.all(),
        label='Выберите категорию новости',
        widget=forms.Select(attrs={'class': 'form-control'})
    )