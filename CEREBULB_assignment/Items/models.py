from django.db import models
from treenode.models import TreeNodeModel

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    code = models.IntegerField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length= 100)
    product_code = models.IntegerField()
    product_img = models.ImageField(upload_to='images/')
    product_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_mfc_date = models.DateField()

    def __str__(self):
        return self.product_name