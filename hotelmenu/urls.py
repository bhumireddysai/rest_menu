from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('sections_menu/', views.sections_menu, name='sections_menu'),
    path('insert_menu', views.insert_menu, name='insert_menu'),
    path('item_mapping', views.item_mapping, name='item_mapping'),
]
