from django.db import models
from django.contrib.auth.models import User



CONDITION_CHOICES = (
    ('New','New'),
    ('Used', "Used"),
    ("NOOB", "Out of Box" ),
    ('Damaged', 'Damaged'),
    ('For Parts','For Parts'),
    ("SAI", 'Sold As Is')
)



class Item(models.Model):
    name = models.CharField(max_length=80)
    item_type = models.CharField(max_length=80)
    item_description = models.CharField(max_length=150)
    item_img = models.ImageField(upload_to='images/', blank=True, null=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=80,blank=True)
    item = models.ManyToManyField(Item, blank=True)
    total = models.PositiveIntegerField(default=0, blank=True)
    
    def __str__(self):
        return self.name

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    shop_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=180)
    inventory = models.ManyToManyField(Inventory, blank=True)
    
    def __str__(self):
        return self.name