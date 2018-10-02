from django.db import models

class Bank(models.Model):
	name    = models.CharField(max_length=500)
	ac_no   = models.CharField(max_length=120)
	branch  = models.CharField(max_length=500)
	ifsc    = models.CharField(max_length=120)
	def __str__(self):
		return self.name

class ShopDetail(models.Model):
	name       = models.CharField(max_length=120)
	gstin      = models.CharField(max_length=120)
	address    = models.CharField(max_length=500,blank=True,null=True)
	bank       = models.ForeignKey(Bank,blank=True,null=True)
	mobile     = models.CharField(max_length=50, blank=True,null=True)
	state_code = models.CharField(max_length=10,blank=True,null=True)


	def __str__(self):
		return self.name


# class Records(models.Model):
