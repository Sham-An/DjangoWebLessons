# from django.db import models
from django.db import models


# Create your models here.

# python manage.py shell
# Bb.objects.create(title='Дом', content='Трехэтажный, кирпич', price=50000000)

# manage.py makemigrations bboard

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


# class Bb(models.Model):
# title=models.CharField(max_length=50,verbose_name='Товар’)
# content= models.TextField(null=True,blank=True,verbose_name='Описание')
# price=models.FloatField(null=True,blank=True,verbose_name='LJeHa')
# published=models.DateTimeFieId(auto_now_add=True,db_index=True,verbose_name='Опубликовано’)
# classMeta:verbose_name_plural='Объявления'verbose_name='Объявление'ordering=['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name



    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
