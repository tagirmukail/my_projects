from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.
def index(request):
    """Домашняя страница приложения Day Book"""
    return render(request, 'journal/index.html')

# Ограничение доступа.
@login_required
def categories(request):
    """Выводит список всех категорий."""
    categories = Category.objects.filter(master=request.user).order_by('date_added')
    context = {'categories': categories}
    return render(request, 'journal/categories.html', context)

@login_required
def category(request, category_id):
    """Выводит категорию и все ее записи."""
    category = Category.objects.filter(master=request.user).get(id=category_id)
    # Проверка пользователя.
    master_valid(request, category)
    entries = category.entry_set.order_by('date_added')
    context = {'category': category, 'entries': entries}
    return render(request, 'journal/category.html', context)

@login_required
def new_category(request):
    """Добавление новой категории пользователем."""
    if request.method != 'POST':
        # Данные не отправленны, создаем пустую форму.
        form = CategoryForm()
    else:
        # Отправили данные Post, обрабатываем данные.
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Данные введены верно.
            new_category = form.save(commit=False)
            new_category.master = request.user
            new_category.save()
            return HttpResponseRedirect(reverse('journal:categories'))

    context = {'form':form}
    return render(request, 'journal/new_category.html', context)

@login_required
def new_entry(request, category_id):
    """Добавляет новую запись по конкретной теме."""
    category = Category.objects.get(id=category_id)
    # проверка пользователя.
    master_valid(request, category)

    if request.method != 'POST':
        # Данные не отправленны, создаем пустую форму
        form = EntryForm()

    else:
        # Данные отправленны POST, обработка данных.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Данные введены верно.
            new_entry = form.save(commit=False)
            new_entry.category = category
            new_entry.category.master = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('journal:category', args=[category_id]))
    context = {'category': category, 'form': form}
    return render(request, 'journal/new_entry.html', context)

@login_required
def edit_entry(request, category_id):
    """ Редактирование существующей записи."""
    entry = Entry.objects.get(id=category_id)
    category = entry.category
    # Проверка пользователя.
    master_valid(request, category)

    if request.method != 'POST':
        #данные не менялись, Форма заполняется данными из текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST, обработка данных.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # данные введены верно.
            # сохранить запись в переменной без добавления в базу данных.
            edit_entry = form.save(commit=False)
            # связывает новую запись с конкретной темой.
            edit_entry.category = category
            # связывает новую запись с конкретным пользователем.
            edit_entry.category.master = request.user
            edit_entry.save()
            return HttpResponseRedirect(reverse('journal:category', args=[category.id]))
    context = {'entry': entry,
               'category': category,
               'form': form}
    return render(request, 'journal/edit_entry.html', context)

def master_valid(request, category):
    # Проверка принадлежности темы конкретному пользователю.
    if category.master != request.user:
        raise Http404