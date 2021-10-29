from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('adapt/<item_id>/', views.adapt_basket, name='adapt_basket'),
]
