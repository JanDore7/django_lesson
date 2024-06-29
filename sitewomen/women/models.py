from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta: # Более подробно см. https://django.fun/docs/django/4.2/ref/models/options/#
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]



# <имя атрибута>__gte - больше или равно (>=)
# <имя атрибута>__lte - меньше или равно (<=)
# <имя атрибута>__gt - юольше (>)
# <имя атрибута>__lt - меньше (<)
# Запросы пример Women.objects.filter(pk__gte=1) - получить все записи с pk больше или равно 1


# Women.objects.create(Обьязательные аргументы) - создать запись
# Women.objects.filter(title__contains='ли') - получить все записи с title которая содержит - ли
# Women.objects.filter(title__icontains='ли') - искать без учета регистра не работает для SQLite
# Women.objects.filter(pk__in[2,5,11,12]) - получить запись с pk 2,5,11,12
# Women.objects.filter(pk__in[2,5,11,12], is_published=True) - получить запись с pk 2,5,11,12 и is_published=True
# Women.objects.exclude(pk=2) - получить все записи кроме 2

# Women.objects.get(pk=2) - возвращает не список, а объект (str) если записи нет, то вернет ошибку. (Использовать при авторизации)


# Сортировка по указанному полю
# Women.objects.order_by('title') - сортировка по title (сортируется в лексикографическом порядке)
# Women.objects.order_by('-title') - сортировка по title (сортируется в обратном лексикографическом порядке)

#Women.objects.filter(pk_lte=4).order_by('title') - получить все записи с pk меньше или равно 4 и сортировать по title

# Меняем данные
# wu = Women.objects.get(pk=2)
# wu.title = 'Марго Робби'
# wu.content = 'Биограффия Марго Робби'
# wu.save()

# Меняем записи во всех данных
# Women.objects.update(is_published=False)

# Меняем выборочно (срез не применяется)
# Women.objects.filter(pk__lte=4).update(is_published=1)

# Метод update применяется только для коллекции QuerySet!

# Удаление записи.
# Women.objects.filter(pk_lte=4).delete()
