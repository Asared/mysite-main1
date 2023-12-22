from django.db import models

# Create your models here.


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='catalog/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name