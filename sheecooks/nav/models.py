from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class User(models.Model):
   #user_id = models.BigAutoField(primary_key=True)
   #user_first_name = models.CharField(max_length =100)
  # user_last_name = models.CharField(max_length = 100)
   #user_email = models.EmailField()
   #user_address = models.CharField(max_length = 150)
  # favorite_items = models.ForeignKey("Product", on_delete= models.RESTRICT, blank=True)
  # profile_pic = models.ImageField(default='default.png', upload_to='images/')
   #def __str__(self):
   #    return self.user_first_name

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

class Toppicks(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    pick_description = models.CharField(max_length = 50)
    pick_photo = models.ImageField(upload_to='images/')
    pick_price = models.DecimalField(max_digits=20, decimal_places=2,blank= False)
    def __str__(self):
       return self.pick_description
    #table to store toppick items in the cart.
class CartItems_toppick(models.Model):
    cart_owner = models.ForeignKey(User, on_delete = models.CASCADE)
    toppick_cart_product = models.ForeignKey(Toppicks, on_delete = models.CASCADE, null = True)
    quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
       return self.toppick_cart_product.pick_description
    
    
    #table to store main menu items in the cart.

class CartItems_menu(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    menu_product_id = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
       return self.menu_product_id.product_name

class checkout_information(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    delivery_address = models.TextField(max_length = 250)
    Card_number = models.CharField(max_length = 15)
    Card_name = models.CharField(max_length = 200)
    expiration_on_card = models.CharField(max_length =15)
    Security_Code = models.PositiveIntegerField()