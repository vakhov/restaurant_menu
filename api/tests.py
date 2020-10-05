import json

from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase

from menus.models import Category, Menu
from utils.helpers import get_image


class ApiTests(APITestCase):
    def setUp(self) -> None:
        self.category: Category = Category.objects.create(title='Горячее')
        self.token: str = settings.TOKEN_KEY

    def test_create_menu(self):
        data = {
            'category': self.category.id,
            'title': 'Шашлык',
            'price': 100.00,
            'calorie': 500,
            'image': None,
            'token': self.token,
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['category'], data['category'])
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(float(response.data['price']), data['price'])
        self.assertEqual(response.data['calorie'], data['calorie'])
        self.assertEqual(response.data['image'], data['image'])
        self.assertEqual(Menu.objects.count(), 1)

    def test_without_token(self):
        data = {
            'title': 'Шашлык',
            'price': 100.00,
            'calorie': 500,
            'image': None,
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_price(self):
        data = {
            'title': 'Шашлык',
            'price': 100000.003,
            'calorie': 500,
            'image': None,
            'token': self.token,
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_without_title(self):
        data = {
            'price': 100.00,
            'calorie': 500,
            'image': None,
            'token': self.token,
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content.decode('utf-8'))['title'][0], 'Это поле обязательно.')

    def test_create_menu_obj(self):
        data = {
            'title': 'Шашлык',
            'price': 100.00,
            'calorie': 500,
            'image': None,
            'token': self.token,
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(json.loads(response.content.decode('utf-8')), {
            'category': None,
            'category_verbose': 'Без категории',
            'title': 'Шашлык',
            'price': '100.00',
            'image': None,
            'calorie': 500
        })

    def test_with_category(self):
        data = {
            'title': 'Шашлык',
            'price': 100.00,
            'calorie': 500,
            'image': None,
            'token': self.token,
            'category': self.category.id
        }
        response = self.client.post('/api/menu/', data=data, format='json')
        self.assertEqual(json.loads(response.content.decode('utf-8')), {
            'category': self.category.id,
            'category_verbose': self.category.title,
            'title': 'Шашлык',
            'price': '100.00',
            'image': None,
            'calorie': 500
        })

    def test_add_image(self):
        data = {
            'title': 'Шашлык',
            'price': 100.00,
            'calorie': 500,
            'image': get_image(),
            'token': self.token,
        }
        response = self.client.post('/api/menu/', data=data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
