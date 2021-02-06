from django_filters import FilterSet # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post
from datetime import datetime
from django.forms import Select, TextInput, SelectMultiple, Textarea

 
 
# создаём фильтр
class NewsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post


        fields = {
            'post_datetime': ['gt'], 
            'post_title': ['icontains'], 'author_post':['in']
        } # поля которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
