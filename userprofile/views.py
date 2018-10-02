from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .forms import UserProfileForm
from django.urls import reverse_lazy,reverse
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate , login , get_user_model , logout

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return  redirect(reverse('profile:profile-page'))

class ProfilePage(ListView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated))# and u.is_staff==False))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    template_name = 'user-profile/profile-page.html'

    def get_queryset(self):
        query = UserProfile.objects.get(user=self.request.user)
        return query