from django.db import models
from tags.models import Tag



class Product(models.Model):
    product = models.CharField(max_length=500)
    type    = models.ForeignKey(Tag, blank=True, null=True)

    def __str__(self):
        return self.product
