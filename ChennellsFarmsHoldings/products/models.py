from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    """
    This class represents a product in the system.

    Attributes:
        name (CharField): The name of the product (max 100 characters).
        price (DecimalField): The price of the product (default 0, with 2 decimal places and max 6 digits).
        description (CharField): A description of the product (optional, max 250 characters).
        image (ImageField): An image file for the product (stored in uploads/product/).
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')


    def __str__(self):
        return str(self.name)


class CartItem(models.Model):
    """
    This class represents an item in a user's shopping cart.

    Attributes:
        user (ForeignKey): The user who owns the cart item.
        product (ForeignKey): The product associated with the cart item.
        quantity (PositiveIntegerField): The quantity of the product in the cart item (default 1).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
