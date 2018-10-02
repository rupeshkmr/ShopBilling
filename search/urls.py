from django.conf.urls import url
from .views import Record
urlpatterns = [
    url(r'^$', Record.as_view(), name='query'),

]

