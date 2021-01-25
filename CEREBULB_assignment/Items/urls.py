from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_view.as_view(), name = 'home'),
    path('product/<int:pk>', views.product_list_view.as_view(), name='detail'),
]