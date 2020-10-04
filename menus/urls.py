from django.urls import path

from .views import CategoryListView, OrderTemplateView

app_name = 'menus'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('order/', OrderTemplateView.as_view(), name='order-view'),
]
