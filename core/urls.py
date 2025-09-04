from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('password_reset', views.password_reset, name='password_reset'),
    path("cart_detail/", views.cart_detail, name="cart_detail"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
]