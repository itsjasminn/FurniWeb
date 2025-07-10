from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from apps.views import LoginFormView, VerifyCodeFormView, ResendCodeView, ContactView, AboutView, ServicesView, \
    HomeView, BlogView, ThanksView, ShopView, CartView, CheckoutView
from root.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('about', AboutView.as_view(), name='about'),
                  path('blog', BlogView.as_view(), name='blog'),
                  path('contact', ContactView.as_view(), name='contact'),
                  path('services', ServicesView.as_view(), name='services'),
                  path('login', TemplateView.as_view(template_name='auth/login.html'), name='login'),
                  path('login/', LoginFormView.as_view(), name='login'),
                  path('verify-code/', VerifyCodeFormView.as_view(), name='verify_code'),
                  path('resend-code/', ResendCodeView.as_view(), name='resend_code'),
                  path('shop', ShopView.as_view(), name='shop'),
                  path('thanks', ThanksView.as_view(), name='thanks'),
                  path('checkout', CheckoutView.as_view(), name='checkout'),
                  path('cart', CartView.as_view(), name='cart'),

              ] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
