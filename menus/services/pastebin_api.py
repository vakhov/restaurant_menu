from menus.services.pastebin import Pastebin
from environ import Env
from django.conf import settings

env = Env()


class PastebinApi:
    def create_paste(self, text: str, title: str) -> str:
        pastbin = Pastebin(settings.PASTBIN_API_DEV_KEY,
                           settings.PASTBIN_API_USER_NAME,
                           settings.PASTBIN_API_USER_PASSWORD)
        return pastbin.create_paste(text, title)
