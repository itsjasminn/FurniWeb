from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from apps.views import home_view, about_view, blog_view, cart_view, checkout_view, index_view, \
    services_view, shop_view, thankyou_view, LoginFormView, VerifyCodeFormView, ResendCodeView, ContactView
from root.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('home', home_view),
                  path('about', about_view, name='about'),
                  path('blog', blog_view, name='blog'),
                  path('cart', cart_view, name='cart'),
                  path('checkout', checkout_view),
                  path('contact', ContactView.as_view(), name='contact'),
                  path('', index_view, name='home'),
                  path('services', services_view, name='services'),
                  path('shop', shop_view, name='shop'),
                  path('thanks', thankyou_view),
                  path('login', TemplateView.as_view(template_name='auth/login.html'), name='login'),
                  path('login/', LoginFormView.as_view(), name='login'),
                  path('verify-code/', VerifyCodeFormView.as_view(), name='verify_code'),
                  path('resend-code/', ResendCodeView.as_view(), name='resend_code'),

              ] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
