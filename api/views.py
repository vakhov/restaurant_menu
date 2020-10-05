from django.conf import settings
from rest_framework import mixins
from rest_framework.exceptions import NotAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.serializers import RestaurantMenuSerializer
from menus.models import Menu


class RestaurantMenuListCreateAPIView(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      GenericViewSet):
    queryset = Menu.objects.filter(category__isnull=False)
    serializer_class = RestaurantMenuSerializer

    def dispatch(self, request, *args, **kwargs):
        token = request.POST.get('token', None) or request.GET.get('token', None)
        if not token or token != settings.TOKEN_KEY:
            raise NotAuthenticated()
        return super().dispatch(request, *args, **kwargs)
