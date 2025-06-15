from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='product_images', blank=True, default='')

    def __str__(self):
        return f'{self.brand}{self.name}'