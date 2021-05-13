from django.urls import path, include
from . import views
from .forms import UserLoginForm
from rest_framework import routers, serializers, viewsets
from .models import CaUser, Product
from rest_framework.authtoken.views import obtain_auth_token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaUser
        fields = ['url', 'username', 'email', 'is_staff']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'picture']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = []
    permission_classes = []

class UserViewSet(viewsets.ModelViewSet):
    queryset = CaUser.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

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
    path('orderform/', views.order_form, name="order_form"),
    path('api/', include(router.urls)),
    path('token/', obtain_auth_token, name="api_token_auth")
]
