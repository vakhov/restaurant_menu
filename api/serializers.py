from rest_framework import serializers

from menus.models import Menu


class RestaurantMenuSerializer(serializers.ModelSerializer):
    """Сериализатор Меню Ресторана"""

    category_verbose = serializers.SerializerMethodField()

    def get_category_verbose(self, obj):
        return obj.category.title if obj.category else 'Без категории'

    class Meta:
        model = Menu
        fields = ('category', 'category_verbose', 'title', 'price', 'image', 'calorie')
