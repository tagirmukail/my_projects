from django.conf.urls import url

from . import views

urlpatterns = [
    # домашняя страница.
    url(r'^$', views.index, name='index'),
    # вывод всех категорий.
    url(r'^categories/$', views.categories, name='categories'),
    # Страница с записями по отдельной категории.
    url(r'^categories/(?P<category_id>\d+)/$', views.category, name='category'),
    # страница для добавления новой темы.
    url(r'^new_category/$', views.new_category, name='new_category'),
    # страница для добавления новой записи
    url(r'^new_entry/(?P<category_id>\d+)/$', views.new_entry, name='new_entry'),
    # страница для редактирования записей.
    url(r'^edit_entry/(?P<category_id>\d+)/$', views.edit_entry, name='edit_entry'),
]