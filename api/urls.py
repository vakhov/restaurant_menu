from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import RestaurantMenuListCreateAPIView

app_name = 'api'

api_router = DefaultRouter()
api_router.register(r'menu', RestaurantMenuListCreateAPIView, basename='menu-api')

urlpatterns = [
    path('', include(api_router.urls)),
]
