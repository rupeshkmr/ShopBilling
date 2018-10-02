from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include

from .views import ProductListView,  UpdateProduct, AddProduct


urlpatterns = [
    url(r'^$', ProductListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', UpdateProduct.as_view(), name='update'),
    url(r'^add-product/$', AddProduct.as_view(), name='add-product'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

