from django import forms

class customerForm(forms.Form):
	mobile_no   = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your mobile number","class":"form-control"}))

