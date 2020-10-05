def pastebin_create(sender, instance=None, created=False, **kwargs):
    if created:
        from menus.tasks import pastebin
        pastebin.apply_async()
