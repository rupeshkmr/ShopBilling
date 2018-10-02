from django.db import models
from items.models import Item


class Bill(models.Model):
	customer   = models.CharField(max_length=60)
	# items      = models.ManyToManyField(Item)
	price      = models.DecimalField(max_digits=2,decimal_places=2)
	invoice_no = models.IntegerField()
	date       = models.DateField(auto_now_add=True)
	time       = models.TimeField(auto_now_add=True)
	discount   = models.DecimalField(max_digits=2,decimal_places=2)
	taxableamt = models.DecimalField(max_digits=2,decimal_places=2)
	GST        = models.DecimalField(max_digits=2,decimal_places=2)
	total      = models.DecimalField(max_digits=2,decimal_places=2)

	def __str__(self):
		return str(self.invoice_no)