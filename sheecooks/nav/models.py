from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.user_first_name
    user_id = models.BigAutoField(primary_key=True)
    user_first_name = models.CharField(max_length =100)
    user_last_name = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_address = models.CharField(max_length = 150)
    favorite_items = models.ForeignKey("Product", on_delete= models.RESTRICT, blank=True)
class Product(models.Model):
    date = models.DateField()
    product_name = models.CharField(max_length = 100)
    product_serial_no = models.BigAutoField(primary_key=True)
    opening_balance = models.IntegerField()
    closing_balance = models.IntegerField()
    sales = models.IntegerField()
    product_buying_price = models.FloatField(max_length =100)
    product_selling_price = models.FloatField(max_length =100)
    sales_tax = models.FloatField(max_length =20)
    sale_discount = models.FloatField(blank = True)
class Order(models.Model):
    date_ordered = models.DateField()
    ordered_by = models.ForeignKey(User, on_delete = models.CASCADE)
    product_ordered = models.ForeignKey(Product, on_delete = models.CASCADE)
