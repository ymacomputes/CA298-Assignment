from django.forms import ModelForm
from .models import Product, CaUser
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class CASignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        return user