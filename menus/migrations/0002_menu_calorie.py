# Generated by Django 3.1.2 on 2020-10-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='calorie',
            field=models.PositiveSmallIntegerField(default=50, verbose_name='Калорийность'),
        ),
    ]