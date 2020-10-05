from django.core.validators import DecimalValidator
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from utils.helpers import generate_upload_name

__all__ = ['Category', 'Allergen', 'Menu', 'PastBinLink']

from utils.models import SingletonModel


class Category(models.Model):
    """
    Категории
    """
    title = models.CharField('Наименование', max_length=50, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ('title',)
        ordering = ('title',)


class Allergen(models.Model):
    """
    Аллергены
    """
    title = models.CharField('Наименование', max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'
        unique_together = ('title',)
        ordering = ('title',)


class Menu(models.Model):
    """
    Меню
    """
    category = models.ForeignKey(Category, models.SET_NULL, 'menu_items', verbose_name='Категория', null=True)
    title = models.CharField('Название', max_length=100, db_index=True)
    price = models.DecimalField('Стоимость', max_digits=5, decimal_places=2, default=350,
                                validators=[DecimalValidator(5, 2)])
    image = ThumbnailerImageField('Изображение', upload_to=generate_upload_name, null=True, blank=True)
    allergens = models.ManyToManyField(Allergen, verbose_name='Аллергены')
    calorie = models.PositiveSmallIntegerField('Калорийность', default=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        unique_together = ('title',)
        ordering = ('category', 'title',)


class PastBinLink(SingletonModel):
    """Ссылка в сервисе Pastbin на меню ресторана"""
    link = models.URLField('Ссылка', blank=True, null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка на меню'
        verbose_name_plural = 'Ссылка на меню'

    def get_pastebin_link(self):
        return self.link if self.link else None
