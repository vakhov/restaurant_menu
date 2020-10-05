from menus.models import PastBinLink


def pastebin_link(request):
    return {'pastebin_link': PastBinLink.load().get_pastebin_link()}
