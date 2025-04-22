from django.urls import path

from apps.cart import views

urlpatterns = [
    path("", views.CartPage.as_view(), name="cart_page"),
    path("add/cart/<int:pk>/", views.add_product, name="add_cart"),
    path("remove/cart/<int:pk>/", views.remove_product, name="remove_cart"),
    path("clear/cart", views.clear_cart, name="clear_cart")
]