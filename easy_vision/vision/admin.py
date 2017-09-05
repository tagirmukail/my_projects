from django.contrib import admin
from .models import Category, Blog
# Register your models here.

# модель категорий блогов
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# модель блога
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'created', 'videourl']
    list_filter = ['created']
    list_editable = ['videourl']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
