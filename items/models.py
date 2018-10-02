from django.db import models
from brands.models import Brand
from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed, pre_init,post_init


class Item(models.Model):
    item       = models.CharField(max_length=120)
    brand      = models.ForeignKey(Brand,blank=True,null=True)
    product    = models.ForeignKey(Product,blank=True,null=True)
    cost_pu    = models.DecimalField(decimal_places=2, max_digits=10)
    hsn        = models.BigIntegerField(unique=True)
    quantity   = models.IntegerField(default = 0)
    meter      = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    tquantity  = models.IntegerField(default=0)
    tmeter     = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    readymade  = models.BooleanField(default=False)

    def __str__(self):
        return self.item


def item_post_save_receiver(sender, instance, *args, **kwargs):
    if(instance.quantity != 0):
        if(instance.readymade == False):
            instance.readymade = True
            instance.tquantity = instance.quantity
            instance.save()
    else:
        if(instance.readymade == True):
            instance.readymade = False
            instance.tquantity = instance.quantity
            instance.save()

post_save.connect(item_post_save_receiver, sender=Item)

class GstDetail(models.Model):
    cgst = models.DecimalField(decimal_places=2, max_digits=4,default=2.5)
    sgst = models.DecimalField(decimal_places=2,max_digits=4,default=2.5)

    def __str__(self):
        return str(self.cgst+self.sgst)