from django.template.loader import render_to_string

from menus.models import Menu, PastBinLink
from menus.services.pastebin_api import PastebinApi
from restaurant_menu.celery import app


@app.task
def pastebin():
    """Постим меню ресторана на Pastebin.com"""
    menu_items = Menu.objects.filter(calorie__isnull=False)
    text = render_to_string('menus/pastebin.html', context={'menu_items': menu_items})
    pastebin_link = PastebinApi().create_paste(text, 'Меню ресторана')
    pasebin_obj = PastBinLink.load()
    pasebin_obj.link = pastebin_link
    pasebin_obj.save()
    return pastebin_link
