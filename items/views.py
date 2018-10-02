from django.shortcuts import render, redirect
from .models import Item, GstDetail
from products.models import Product
from brands.models import Brand
from tags.models import Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


class ItemListView(ListView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    template_name = 'items/item_list.html'
    queryset = Item.objects.all()

class UpdateItem(UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    template_name = 'items/update-item.html'
    model = Item
    fields = ["item","brand","product","cost_pu","hsn","quantity","meter"]
    success_url = reverse_lazy("items:item-list")

class AddItem(CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    template_name = "items/add-item.html"
    model = Item
    fields = ["item", "brand", "product", "cost_pu", "hsn", "quantity","meter"]
    success_url = reverse_lazy("items:add-item")

    def form_valid(self,form):
        obj = form.save(commit=False)
        if(obj.quantity == 0):
            obj.tmeter = obj.meter
            obj.save()
        else:
            obj.save()
        return redirect("items:add-item")