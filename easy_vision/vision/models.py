from django.db import models
from django import forms
from django.core.urlresolvers import reverse

# модель категорий
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True)
    class Meta:
        ordering = ['name',]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vision:BlogListByCategory', args=[self.slug])

# модель статьи
class Blog(models.Model):
    category = models.ForeignKey(Category, related_name='blogs', verbose_name='Категория')
    name = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    videourl = models.URLField(max_length=250, verbose_name='Видео url',default=None)
    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Блоги'
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name
    # возвращает урл статьи
    def get_absolute_url(self):
        return reverse('vision:BlogDetail', args=[self.id, self.slug])

# модель создания статьи
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('created',)