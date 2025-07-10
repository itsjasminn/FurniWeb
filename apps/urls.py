from django.conf.urls.static import static
from django.urls import path

from apps.views import home_view, about_view, blog_view, cart_view, checkout_view, contact_view, index_view, \
    services_view, shop_view, thankyou_view
from root.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('home', home_view),
                  path('about', about_view, name='about'),
                  path('blog', blog_view, name='blog'),
                  path('cart', cart_view, name='cart'),
                  path('checkout', checkout_view),
                  path('contact', contact_view, name='contact'),
                  path('', index_view, name='home'),
                  path('services', services_view, name='services'),
                  path('shop', shop_view, name='shop'),
                  path('thanks', thankyou_view),

              ] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
