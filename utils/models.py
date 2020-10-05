from django.db import models


class SingletonModel(models.Model):
    """ Singleton для настрок и т.п. """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """ Загрузка единственной записи под id = 1 """
        obj, create = cls.objects.get_or_create(pk=1)
        return obj
