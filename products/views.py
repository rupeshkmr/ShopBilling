from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class ProductListView(ListView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    queryset = Product.objects.all()
    template_name = "products/list.html"

class AddProduct(CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Product
    template_name = 'products/product_form.html'
    fields = ["product","type"]
    success_url = reverse_lazy('products:list')

class UpdateProduct(UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Product
    template_name = 'products/product_form.html'
    fields = ["product","type"]
    success_url = reverse_lazy('products:list')

