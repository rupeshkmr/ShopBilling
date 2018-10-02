from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin


from .views import home_page, about_page, contact_page, login_page, register_page,logout_page

urlpatterns = [
    url(r'^$', home_page,name="home"),
    url(r'^about/$', about_page),
    url(r'^contact/$', contact_page),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^register/$', register_page,name='register'),
    url(r'^products/', include("products.urls", namespace="products")),
    url(r'^receipt/', include("receipt.urls", namespace="receipt")),
    url(r'^admin/', admin.site.urls),
    url(r'^items/', include("items.urls", namespace="items")),
    url(r'^shop/', include("shop.urls", namespace="shop")),
    url(r'^brands/', include("brands.urls", namespace="brands")),
	url(r'^profile/', include("userprofile.urls", namespace="profile")),
    url(r'^search/', include("search.urls", namespace="search")),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

