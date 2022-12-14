from django.urls import path
from .views import ItemListView, ItemCreateView
urlpatterns = [
    path('list', ItemListView.as_view(), name='list_items'),
    path('create', ItemCreateView.as_view(), name='create_item'),
]
