from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.register, name="register"),
    path('allproducts', views.all_products, name="all_products"),
    path('singleproduct/<int:prodid>', views.singleproduct, name="product_single"),
    path('myform/', views.myform),
    path('usersignup/', views.CaUserSignupView.as_view(), name="register")
]
