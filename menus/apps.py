from django.apps import AppConfig
from django.db.models.signals import post_save

from .signals import pastebin_create


class MenusConfig(AppConfig):
    name = 'menus'
    verbose_name = 'Меню'

    def ready(self):
        from .models import Menu
        post_save.connect(pastebin_create, Menu, dispatch_uid='Menu_pastebin_create')
