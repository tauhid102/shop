from django.db import models

#  Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField
MinValueValidator
STATE_CHOICES = (
    ('Dhaka & Uttara', 'Dhaka & Uttara'),
    ('Mirpur', 'Mirpur'),
    ('Dhanmondi', 'Dhanmondi'),
    ('Ware', 'Ware'),
    ('Gulistan', 'Gulistan'),
    ('Motizhil', 'Motizhil'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
def _str_(self):
    return str(self.id)

CATEGORY_CHOICE = (
    ('w', 'Women Care'),
    ('B', 'Baby Care'),
    ('S', 'Skin Care'),
    ('p','Personal Care'),
    ('Or','Orthopedic'),
    ('D','Diabetice'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    Category = models.CharField(choices = CATEGORY_CHOICE, max_length=4) 
    product_image = models.ImageField(upload_to = 'productimg')
def _str_(self):
    return str(self.id)

class Cart(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     Product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)

def _str_(self):
     return str(self.id)

@property
def total_cost(self):
 return self.quantity * self.Product.discounted_price


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Pending')
def _str_(self):
    return str(self.id) 
@property
def total_cost(self):
 return self.quantity * self.Product.discounted_price