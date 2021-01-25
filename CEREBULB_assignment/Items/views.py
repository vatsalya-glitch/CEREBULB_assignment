from django.views.generic import ListView
from .models import Category, Product

# Create your views here.
class category_list_view(ListView):
    model = Category
    template_name = 'home.html'

class product_list_view(ListView):
    model = Product
    template_name = 'home.html'