import io
import os
from hashlib import md5
from os import path as op
from time import time

from PIL import Image
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer


def generate_upload_name(instance, filename, prefix=None, unique=False):
    """Auto generate name for File and Image fields."""
    ext = op.splitext(filename)[1]
    name = str(instance.pk or '') + filename + (str(time()) if unique else '')

    filename = md5(name.encode('utf8')).hexdigest() + ext
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    if prefix:
        basedir = op.join(basedir, prefix)
    return op.join(basedir, filename[:2], filename[2:4], filename)


def thumbnail_column(size='106x80', **kwargs):
    """Формирование картинки для анонса в админке"""

    field = kwargs.pop('field', 'image')
    crop = kwargs.pop('crop', 'center')
    quality = kwargs.pop('quality', 99)
    width, heigth = size.split('x')

    def real_decorator(function):
        def wrapper(self, inst):
            images = [getattr(inst, field, None)]
            result = function(self, inst)
            if result is not None:
                if isinstance(result, (list, tuple)):
                    images.extend(result)
                else:
                    images.append(result)

            import logging
            logger = logging.getLogger(__name__)
            for image in images:
                try:
                    if image:
                        thumbnailer = get_thumbnailer(image)
                        im = thumbnailer.get_thumbnail({'quality': quality, 'crop': crop, 'size': (width, heigth)})
                        return mark_safe(f'<img src="{im.url}" width="{im.width}" height="{im.height}" />')
                except Exception as e:
                    logger.debug(e)
            return '(Картинки нет)'

        wrapper.admin_order_field = field
        wrapper.short_description = kwargs.pop('short_description', 'Изображение')
        for key, value in kwargs.items():
            setattr(wrapper, key, value)
        return wrapper

    return real_decorator


def get_image():
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(255, 255, 255))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file
