from django.conf import settings
from rest_framework import mixins
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import GenericViewSet

from api.serializers import RestaurantMenuSerializer
from menus.models import Menu


class TokenRequired(BasePermission):

    def has_permission(self, request, view):
        token = request.data.get('token') or request.POST.get('token') or request.GET.get('token')
        if not token or token != settings.TOKEN_KEY:
            return False
        return True


class RestaurantMenuListCreateAPIView(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      GenericViewSet):
    """Добавление и просмотр меню"""
    queryset = Menu.objects.filter(category__isnull=False)
    serializer_class = RestaurantMenuSerializer
    permission_classes = (TokenRequired,)
