from django.db import models
#from products.models import Product
from gst.utils import unique_order_id_generator
from django.db.models.signals import pre_save, post_save
from items.models import Item
from shop.models import ShopDetail

class Cart(models.Model):
	invoice_no  = models.IntegerField(default=0)
	item        = models.ForeignKey(Item,on_delete=None, null=True,blank=True)
	quantity    = models.IntegerField(default=0)
	meter       = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
	discount    = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
	price       = models.DecimalField(max_digits=10, decimal_places=4,default=0.00)
	hsn         = models.IntegerField(default=0)

	def __str__(self):
		return str(self.invoice_no)

	# def save(self, force_insert=False, force_update=False):
	# 	self.price = self.item.cost_pu * self.quantity
	# 	self.price = self.price - (self.discount * self.price) / 100
	# 	super(Cart, self).save(force_insert, force_update)
# def post_save_receiver(sender, instance, *args, **kwargs):
# 	object = Cart.objects.get(id=instance.id)
# 	object.price = instance.item.cost_pu * instance.quantity
# 	object.save()


# post_save.connect(post_save_receiver, sender = Cart)

# def pre_save_update(sender, instance, *args, **kwargs):
#     # if not instance.order_id:
#     #    instance.order_id = unique_order_id_generator(instance)
# 	instance.cgst = instance.item.cgst


# pre_save.connect(pre_save_update, sender=Cart)

class Customer(models.Model):
	name      = models.CharField(max_length=120,default="Cash")
	mobile_no = models.CharField(max_length=15,blank=True,null=True)
	address   = models.CharField(max_length=500,blank=True,null=True)

	def __str__(self):
		return self.name




class Bill(models.Model):
	invoice_no      = models.IntegerField()
	customer_info   = models.ForeignKey(Customer,unique=False,null=True,blank=True)
	shop_details    = models.ForeignKey(ShopDetail, on_delete=None,null=True, blank=True)
	cart_item       = models.ManyToManyField(Cart, null=True,blank=True)
	sub_total       = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	total           = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	cgst            = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	sgst            = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	igst            = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	additional_disc = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	time            = models.DateField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return str(self.invoice_no)

	# def save(self, force_insert=False, force_update=False):
	# 	queryset = Base.objects.filter(invoice_no=self.invoice_no)
	# 	super(Bill, self).save(force_insert, force_update)


