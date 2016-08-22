# coding: utf-8
from django.contrib import admin
from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'views', 'likes')
    search_fields = ('name',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ('category',)
    list_per_page = 10
    search_fields = ('title', 'category__name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

