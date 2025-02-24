from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), 
    path("flavors/", views.flavors, name="flavors"),
    path("order/", views.order_icecream, name='order_icecream'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    ]