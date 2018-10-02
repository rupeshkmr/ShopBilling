from django.shortcuts import render
from .models import Bank, ShopDetail
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class ShopDetails(ListView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "shop/shop_detail.html"
	queryset = ShopDetail.objects.all()

class UpdateDetails(UpdateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "shop/update_shop.html"
	model = ShopDetail
	fields = ["name","gstin","bank"]
	success_url = reverse_lazy("shop:shop-detail")

class BankDetails(CreateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "shop/bank.html"
	model = Bank
	fields = ["ac_no","branch","ifsc","name"]
	success_url = reverse_lazy("shop:shop-detail")