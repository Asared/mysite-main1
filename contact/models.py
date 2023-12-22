from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    map_location = models.URLField()
    map_embed_code = models.TextField(default='MAP')

    def __str__(self):
        return f'{self.address} - {self.phone}'