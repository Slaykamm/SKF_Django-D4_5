from django.forms import ModelForm
from .models import Post
from django import forms
from django.forms import Select, TextInput, SelectMultiple, Textarea
 
 

# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['post_title', 'article_text', 'rating_article',  'position', 'author_post',]

        widgets = {
            'post_title': TextInput(attrs={'class': 'form-control'}),


            'article_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...',
                'title': 'AAAAAAAAA',
                
            }),
            'author_post': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Выбрать автора'
            }),
            'position': SelectMultiple(attrs={
                'multiple class': 'form-control',
            }),
        }


