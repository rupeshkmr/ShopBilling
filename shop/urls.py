from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import ShopDetails,UpdateDetails,BankDetails

urlpatterns = [
    url(r'^$', ShopDetails.as_view(), name='shop-detail'),
    url(r'^bank$', BankDetails.as_view(), name='bank'),
    url(r'^(?P<pk>\d+)/$', UpdateDetails.as_view(), name='update-detail'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

