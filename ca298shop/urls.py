from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('all_items/', views.all_items, name="all_items"),
    path('sizes/', views.sizes, name="sizes"),
    path('item/<int:item_id>/', views.view_single_item, name="view_single_item"),
    path('sizes/<str:size>/', views.view_by_size, name="view_by_size"),
    path('create_item/', views.create_item, name="create_item"),
]

