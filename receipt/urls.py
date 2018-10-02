from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from .views import CreateCart,  UpdateBill, UpdateCustomer,  CustomerForm, Invoice, cart_update
urlpatterns = [
    url(r'^create-cart/$', CreateCart.as_view(), name='create-cart'),
    url(r'^(?P<pk>\d+)/$', UpdateBill.as_view(), name='update-bill'),
    url(r'^update-customer/(?P<pk>\d+)/$', UpdateCustomer.as_view(), name='update-customer'),
    url(r'^new-bill/$', CustomerForm.as_view(), name='new-bill'),
    url(r'^invoice/(?P<pk>\d+)/$', Invoice.as_view(), name='invoice'),
    url(r'^cart-update/$', cart_update , name='cart-update'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

