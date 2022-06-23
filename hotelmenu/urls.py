from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('sections_menu/', views.sections_menu, name='sections_menu'),
    path('insert_menu_sections', views.insert_menu_sections, name='insert_menu_sections'),
    path('insert_menu_items', views.insert_menu_items, name='insert_menu_items'),
    path('insert_menu_modifiers', views.insert_menu_modifiers, name='insert_menu_modifiers'),
    path('item_mapping', views.item_mapping, name='item_mapping'),
]