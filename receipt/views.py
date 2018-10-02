from django.shortcuts import render
from django.http import HttpResponse
from .models import Bill, Cart,  Customer
from items.models import GstDetail, Item
from .forms import customerForm
from shop.models import ShopDetail
from django.shortcuts import redirect
#from products.models import Product
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class UpdateBill(UpdateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


	model = Bill
	template_name = 'receipt/bill_form.html'
	fields = ['customer_info']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		return redirect(reverse_lazy("receipt:invoice",kwargs={'pk':obj.id}))

class UpdateCustomer(UpdateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


	model = Customer
	template_name = 'receipt/customer_form.html'
	fields = ['name','address']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		invoice_no = Bill.objects.all().count()
		bill = Bill.objects.create(invoice_no=invoice_no+1,customer_info=obj,shop_details=ShopDetail.objects.get())
		print(bill)
		obj.save()
		return redirect(reverse_lazy("receipt:update-bill",kwargs={"pk":bill.id}))


class CreateCart(CreateView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


	model = Cart
	template_name = 'receipt/cart_form.html'
	fields = ['item','quantity','meter','discount']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		obj.item = Item.objects.get(item=obj.item)
		obj.price = obj.item.cost_pu * obj.quantity + obj.item.cost_pu * obj.meter
		invoice_no = Bill.objects.all().count()
		obj.invoice_no = invoice_no
		obj.save()
		bill = Bill.objects.get(invoice_no=invoice_no)
		bill.cart_item.add(obj)
		itemobj = Cart.objects.filter(item=obj.item)
		mtr = 0
		quan = 0
		for oj in itemobj:
			mtr += oj.meter
			quan += oj.quantity
		obj.item.quantity = obj.item.tquantity - quan
		obj.item.meter = obj.item.tmeter - mtr
		obj.item.save()
		object_list = Cart.objects.filter(invoice_no=invoice_no)
		total = 0
		for object in object_list:
			total += object.price
		bill.additional_disc = obj.discount
		bill.total = total - (bill.additional_disc * total) / 100
		gst = GstDetail.objects.first()
		sgst = gst.sgst
		cgst = gst.cgst
		bill.sgst = total * sgst / 100
		bill.cgst = total * cgst / 100
		bill.igst = bill.cgst + bill.sgst
		bill.sub_total = round(total + bill.sgst + bill.cgst,0)
		bill.save()
		return redirect(reverse("receipt:invoice", kwargs={'pk':bill.id}))
@login_required
def cart_update(request):
	id = request.POST.get('cart_id')
	object = Cart.objects.get(id=id)
	itemobj = Item.objects.get(item=object.item)
	itemobj.meter += object.meter
	itemobj.quantity += object.quantity
	itemobj.save()
	invoice_no = object.invoice_no
	object.delete()
	bill = Bill.objects.get(invoice_no=invoice_no)
	bill.total -= object.price
	object_list = Cart.objects.filter(invoice_no=invoice_no)
	total = 0
	for obj in object_list:
		total += obj.price
	gst = GstDetail.objects.first()
	sgst = gst.sgst
	cgst = gst.cgst
	bill.sgst = total * sgst / 100
	bill.cgst = total * cgst / 100
	bill.igst = bill.cgst + bill.sgst
	bill.sub_total = round(total + bill.sgst + bill.cgst, 0)

	bill.save()
	return redirect(reverse("receipt:invoice", kwargs={'pk':bill.id}))

class CustomerForm(FormView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	template_name = "receipt/new-customer_form.html"
	form_class = customerForm
	success_url = reverse_lazy('receipt:create-customer')

	def form_valid(self,form):
		obj = form.cleaned_data['mobile_no']
		try:
			object = Customer.objects.get(mobile_no=obj)
		except:
			object = None
		if (object is not None):
			invoice_no = Bill.objects.all().count()
			obj = Bill.objects.create(customer_info=object, invoice_no=invoice_no + 1,  shop_details=ShopDetail.objects.get())
			return redirect(reverse('receipt:update-bill', kwargs={'pk': obj.pk}))
		else:
			object = Customer.objects.create(mobile_no=obj)
			return redirect(reverse('receipt:update-customer', kwargs={'pk':object.pk}))


class Invoice(DetailView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


	template_name = 'receipt/invoice.html'
	queryset = Bill.objects.all()

	def get_date(self,request):
		form = dateForm(request.POST or None)
		context = {'form':form}
		if form.is_valid():
			date = form.cleaned_data['date']
			return date

