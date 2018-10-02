from django.conf.urls import url
from .views import user_profile,  ProfilePage

urlpatterns = [
    url(r'^user-profile/$', user_profile, name='user-profile'),
    url(r'^profile-page/$', ProfilePage.as_view(), name='profile-page'),

]

