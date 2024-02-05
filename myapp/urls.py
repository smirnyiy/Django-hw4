from django.urls import path
from .views import user_form, many_fields_form, add_product_info

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('product/', add_product_info, name='add_product_info'),
]
