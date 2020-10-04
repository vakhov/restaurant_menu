from django.shortcuts import render
from django.views.generic import ListView

from menus.models import Category


class CategoryListView(ListView):
    """Список категорий и их значений (меню)"""
    model = Category
    queryset = Category.objects.prefetch_related('menu_items')
