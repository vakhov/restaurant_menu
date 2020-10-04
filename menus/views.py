from django.db.models import Sum
from django.views.generic import ListView, TemplateView

from menus.models import *


class CategoryListView(ListView):
    """Список категорий и их значений (меню)"""
    model = Category
    queryset = Category.objects.prefetch_related('menu_items')


class OrderTemplateView(TemplateView):
    template_name = 'menus/order.html'

    def post(self, request, **kwargs):
        menu_ids = dict(request.POST).get('menu', [])
        menu_items = Menu.objects.filter(id__in=menu_ids)
        allergens = Allergen.objects.filter(menu__in=menu_items).distinct()
        context = {
            'menu_items': menu_items,
            'allergens': allergens,
            'amount': menu_items.aggregate(Sum('price'))['price__sum']
        }

        return super().render_to_response(context)
