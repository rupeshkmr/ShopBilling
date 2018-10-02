from django.shortcuts import render
from django.views.generic import ListView
from receipt.models import Bill, Cart, Customer
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class Record(ListView):
	@method_decorator(user_passes_test(lambda u: u.is_authenticated))  # and u.is_staff==False))
	def dispatch(self, *args, **kwargs):
	    return super().dispatch(*args, **kwargs)

	template_name = 'search/view.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Record, self).get_context_data(*args,**kwargs)
		context['query'] = self.request.GET.get('q')
		return context
	
	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q',None)
		if query is not None:
			try:
				query = datetime.strptime(query, '%d-%m-%Y')
				return Bill.objects.filter(time=query)
			except:
				return None
