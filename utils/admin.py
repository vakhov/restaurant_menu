from django.contrib import admin


class SingletonModelAdmin(admin.ModelAdmin):
    """ Настройки в административной части для Singleton моделей """

    def has_add_permission(self, request):
        """ Убираем кнопку создать, если уже есть одна запись """
        if self.model.objects.count() > 0:
            return False
        return True
