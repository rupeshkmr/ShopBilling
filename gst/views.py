from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from .forms import ContactForm, LoginForm, RegisterForm
from userprofile.models import UserProfile
def home_page(request):
    context = {
        "title":"HOME PAGE",
        "content":"GST WEBAPP",

    }
    if request.user.is_authenticated():
        context["premium_content"] : "Yeahhh"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "ABOUT PAGE",
        "content": "about"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the Contact Page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    if request.user.is_authenticated():
        return redirect("/")

    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("error")
    return render(request, "auth/login.html", context)

def logout_page(request,*args,**kwargs):
    if request.user.is_authenticated():
        logout(request,*args,**kwargs)
        return redirect("/login/")
    else:
        return redirect("/login/")


User = get_user_model()
def register_page(request):
    if request.user.is_authenticated():
        return redirect("/")

    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        UserProfile.objects.create(user=new_user,name=new_user.username)
        login(request,new_user)
        return redirect(reverse('profile:profile-page'))
    return render(request, "auth/register.html", context)
