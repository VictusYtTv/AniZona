from django.db import models
from django.shortcuts import reverse

class Card(models.Model):
  title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
  slug = models.SlugField(max_length=150, unique=True, verbose_name='Тег')
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, max_length=100, verbose_name='Картинка')
  header = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
  body = models.TextField(max_length=200, blank=True, db_index=True, verbose_name='Описание')
  janre = models.ManyToManyField('Janre', blank=True, related_name='cards', verbose_name='Жанр')
  is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
  
  def get_absolute_url(self):
    return reverse('card_page_url', kwargs={'slug': self.slug})

  def __str__(self):
    return '{}'.format(self.title)

  class Meta:
    verbose_name= 'Карточка' 
    verbose_name_plural= 'Карточки' 
    ordering=['header']

class Janre(models.Model):
  title = models.CharField(max_length=50, db_index=True, verbose_name='Наименование жанра')
  slug = models.SlugField(max_length=50, unique=True, verbose_name='Тег')
    
  def __str__(self):
    return '{}'.format(self.title)

  class Meta:
    verbose_name= 'Жанр' 
    verbose_name_plural= 'Жанры' 
    ordering=['title']