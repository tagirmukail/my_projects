from django import forms

from .models import *

class CategoryForm(forms.ModelForm):
    """Форма для заполнения пользователем данных о категориях."""
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'input category'}

class EntryForm(forms.ModelForm):
    """ Форма для заполнения данных о записи"""
    class Meta:
        model = Entry
        fields = ['name', 'description']
        labels = {'name': '',
                  'description': ''}
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}
