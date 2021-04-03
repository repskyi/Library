from django.urls import path
from . import views

urlpatterns = [
    path('orders/',views.addOrders, name = 'addOrders'),
    path('order-id-<int:id>/', views.editOrder, name = 'editOrder'),
    path('close-order-<int:id>/', views.closeOrder, name = 'closeOrder'),
    path('update-order-<int:id>/', views.closeOrder, name = 'updateOrder'),
]
