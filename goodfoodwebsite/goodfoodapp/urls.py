from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.register, name="register"),
    path('allproducts/', views.all_products, name="all_products"),
    path('product/<int:prodid>', views.singleproduct, name="product_single"),
    path('myform/', views.myform),
    path('usersignup/', views.CaUserSignupView.as_view(), name="CaUser register"),
    path('adminsignup/', views.AdminSignupView.as_view(), name="Admin register"),
    path('login/', views.Login.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('addbasket/<int:prodid>', views.add_to_basket, name="add_to_basket"),
    path('basket/', views.get_basket, name="basket"),
    path('ordercomplete/', views.order_form, name="order_complete"),
    path('orderform/', views.order_form, name="order_form")
]
