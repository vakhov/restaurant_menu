from django.contrib import admin

from .models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = list_display
    search_fields = ('id', 'title',)
    list_filter = ('title',)


@admin.register(Allergen)
class AdminAllergen(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = list_display
    search_fields = ('id', 'title',)
    list_filter = ('title',)


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price',)
    list_display_links = ('id', 'title', 'category',)
    list_editable = ('price',)
    list_filter = ('title', 'category', 'price',)
    raw_id_fields = ('category',)
    filter_horizontal = ('allergens',)
