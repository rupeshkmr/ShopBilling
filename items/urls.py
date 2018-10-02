from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include

from .views import ItemListView, UpdateItem, AddItem

urlpatterns = [
    url(r'^item-list/$', ItemListView.as_view(),name='item-list'),
    url(r'^(?P<pk>\d+)/$', UpdateItem.as_view(), name='update-item'),
    url(r'^add-item/$', AddItem.as_view(), name='add-item'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

