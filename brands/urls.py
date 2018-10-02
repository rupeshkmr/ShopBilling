from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import BrandDetails,AddBrand,UpdateBrand

urlpatterns = [
    url(r'^$', BrandDetails.as_view(), name='list'),
    url(r'^add-brand$', AddBrand.as_view(), name='add-brand'),
    url(r'^(?P<pk>\d+)/$', UpdateBrand.as_view(), name='update-detail'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

