from django.urls import path
from .views import goods_list, goods_detail, goods_create, goods_update

urlpatterns = [
    path('', goods_list, name='goods_list'),
    path('<int:pk>', goods_detail, name='goods_detail'),
    path('create/', goods_create, name='goods_create'),
    path('<int:pk>/update/', goods_update, name='goods_update'),
]