# coding: utf-8

from django import forms
from .models import Category, Page


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('category', 'title', 'url')







