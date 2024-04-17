from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
   date = models.DateField()
   product_name = models.CharField(max_length = 100)
   product_serial_no = models.BigAutoField(primary_key=True)
   opening_balance = models.IntegerField(blank = True)
   closing_balance = models.IntegerField(blank = True)
   sales = models.IntegerField(blank = True)
   product_buying_price = models.DecimalField(max_digits =100, decimal_places=2)
   product_selling_price = models.DecimalField(max_digits =100, decimal_places=2)
   sales_tax = models.FloatField(max_length =20)
   sale_discount = models.FloatField(blank = True)
   photo = models.ImageField(upload_to='images/')
   def __str__(self):
       return self.product_name
   

class Order(models.Model):
   date_ordered = models.DateField()
   product_ordered = models.ForeignKey(Product, on_delete = models.CASCADE)
   ordering_client = models.ForeignKey(User, on_delete = models.CASCADE)
   def __str__(self):
       return self.product_ordered


class Splice_display(models.Model):
    splice_photo = models.ImageField(upload_to='images/')
    splice_description = models.CharField(max_length =200)
    def __str__(self):
       return self.splice_description

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    cart_product_id = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    class meta:
            unique_together = ('user', 'cart_product_id')
    def __str__(self):
       return self.cart_product_id.product_name

class checkout_information(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    delivery_address = models.TextField(max_length = 250)
    Card_number = models.CharField(max_length = 15)
    Card_name = models.CharField(max_length = 200)
    expiration_on_card = models.CharField(max_length =15)
    Security_Code = models.PositiveIntegerField()
