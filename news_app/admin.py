from django.contrib import admin
from .models import Category, News, Contact
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    search_fields = ['title']
    list_filter = ['status', 'created_time']
    prepopulated_fields = {"slug": ('title', )}
    date_hierarchy = 'publish_time'
    ordering = ['status', 'publish_time', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Contact)
class CantactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']