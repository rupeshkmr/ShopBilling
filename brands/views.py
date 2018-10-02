from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Brand
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class BrandDetails(ListView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "brands/list.html"
	queryset = Brand.objects.all()

class AddBrand(CreateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "brands/add-brand.html"
	model = Brand
	fields = ['name','owner']
	success_url = reverse_lazy("brands:list")

class UpdateBrand(UpdateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "brands/add-brand.html"
	model = Brand
	fields = ['name','owner']
	success_url = reverse_lazy("brands:list")