# Generated by Django 3.1.2 on 2020-10-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menu_calorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastBinLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
