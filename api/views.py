from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.serializers import RestaurantMenuSerializer
from menus.models import Menu


class RestaurantMenuListCreateAPIView(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      GenericViewSet):
    queryset = Menu.objects.filter(category__isnull=False)
    serializer_class = RestaurantMenuSerializer
