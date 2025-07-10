from django.shortcuts import render

from apps.models import Product


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    return render(request, 'blog.html')


def cart_view(request):
    return render(request, 'cart.html')


def checkout_view(request):
    return render(request, 'checkout.html')


def contact_view(request):
    return render(request, 'contact.html')


def index_view(request):
    return render(request, 'index.html')


def services_view(request):
    return render(request, 'services.html')


def shop_view(request):
    data = {"products": Product.objects.all()}
    return render(request, 'shop.html', data)


def thankyou_view(request):
    return render(request, "thankyou.html")
