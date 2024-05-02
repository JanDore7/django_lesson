from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



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




