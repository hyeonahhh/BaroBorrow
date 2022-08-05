from msilib.schema import Condition
from django.db import models
from accounts.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=256)
    list_price = models.IntegerField()
    deposit = models.IntegerField()
    rental_fee = models.IntegerField()
    explanation = models.TextField()
    condition = models.IntegerField()
    address = models.TextField()
    detail_address =  models.TextField()
    product_photo = models.ImageField(blank=True, null=True, upload_to='product_photo')

    def __str__(self):
        return self.item_name

class BarrowItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    overdue_period = models.IntegerField()
    is_return = models.BooleanField()