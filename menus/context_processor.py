from menus.models import PastBinLink


def pastebin_link(request):
    """Ссылка на меню в Pastebin.com"""
    return {'pastebin_link': PastBinLink.load().get_pastebin_link()}
