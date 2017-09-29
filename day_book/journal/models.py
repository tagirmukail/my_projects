from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """Категории записей дневника"""
    name = models.CharField(max_length=200, verbose_name='Категории')
    date_added = models.DateTimeField(auto_now_add=True)
    # Связь с конкретным пользователем.
    master = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        """строковое представление"""
        return self.name

class Entry(models.Model):
    """Модель записи по категории."""
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=250, verbose_name='Запись')
    description = models.TextField(verbose_name='Описание')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        if len(self.description) > 50:
            return self.name.upper() + '------'+ self.description[:50]+'.......'
        else:
            return self.name.upper() + '------'+ self.description