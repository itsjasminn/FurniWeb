import random
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.views.generic import View, TemplateView, ListView
from redis import Redis

from apps.forms import EmailForm, LoginModelForm
from apps.models import Product, ContactDetails, TeamMember
from apps.models import User
from root.settings import EMAIL_HOST_USER
from .forms import MessageForm
from .models import Message


class LoginFormView(FormView):
    form_class = EmailForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('verify_code')

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        verify_code = random.randrange(10 ** 5, 10 ** 6)
        send_mail(
            subject="Verification Code!",
            message=f"{verify_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
        redis = Redis()
        redis.set(email, verify_code)
        redis.expire(email, time=timedelta(minutes=5))

        return render(self.request, 'auth/verify_code.html', {"email": email})

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


class VerifyCodeFormView(FormView):
    form_class = LoginModelForm
    template_name = 'auth/verify_code.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        sms_code = str(form.cleaned_data.get('sms'))
        redis = Redis()
        redis_code = redis.get(email)

        if not redis_code:
            messages.error(self.request, "Kod muddati tugagan.")
            return redirect('login')

        if int(redis_code) != int(sms_code):  # noqa
            messages.error(self.request, "Kod noto‘g‘ri.")
            return redirect('verify_code')

        user, created = User.objects.get_or_create(email=email)

        if created:
            user.set_unusable_password()
            user.save()
            messages.success(self.request, "Foydalanuvchi muvaffaqiyatli yaratildi va tizimga kirdingiz.")
        else:
            messages.success(self.request, "Tizimga muvaffaqiyatli kirdingiz.")

        login(self.request, user)
        return redirect('home')

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


@method_decorator(csrf_exempt, name='dispatch')
class ResendCodeView(FormView):
    def post(self, request, *args, **kwargs):
        email = request.session.get('pending_email')

        if not email:
            return JsonResponse({
                'success': False,
                'message': 'No pending verification found.'
            })

        verify_code = random.randrange(100000, 999999)

        try:
            send_mail(
                subject="Furniture - Verification Code (Resent)",
                message=f"Your new verification code is: {verify_code}\n\nThis code will expire in 5 minutes.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )

            redis_client = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                decode_responses=True
            )
            redis_client.setex(f"verify_code:{email}", timedelta(minutes=5), verify_code)

            return JsonResponse({
                'success': True,
                'message': 'New verification code sent!'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Failed to resend verification code.'
            })


class ContactView(View):
    template_name = 'menus/contact.html'
    form_class = MessageForm

    def get(self, request, *args, **kwargs):
        contact_details = ContactDetails.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'contact_details': contact_details})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            message_instance = Message(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            if message_instance.write():
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            else:
                messages.error(request, 'Failed to save your message. Please check your input.')
        else:
            messages.error(request, 'Please correct the errors below.')
        contact_details = ContactDetails.objects.all()
        return render(request, self.template_name, {'form': form, 'contact_details': contact_details})


class AboutView(View):
    template_name = 'menus/about.html'

    def get(self, request, *args, **kwargs):
        team_members = TeamMember.objects.all()
        return render(request, self.template_name, {'team_members': team_members})


class ServicesView(TemplateView):
    template_name = 'menus/services.html'


class HomeView(ListView):
    template_name = 'menus/index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


class BlogView(TemplateView):
    template_name = 'menus/blog.html'


class ThanksView(TemplateView):
    template_name = 'menus/thankyou.html'


class ShopView(View):
    template_name = 'menus/shop.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            if product.quantity > 0:
                cart = request.session.get('cart', {})
                cart[product_id] = cart.get(product_id, 0) + 1
                request.session['cart'] = cart
                messages.success(request, f"Added {product.name} to cart!")
            else:
                messages.error(request, "This product is out of stock.")
            return redirect('shop')
        return render(request, self.template_name, {'products': Product.objects.all()})


class CartView(View):
    template_name = 'menus/cart.html'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        cart_items = []
        total = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            if quantity <= product.quantity:
                cart_items.append({'product': product, 'quantity': quantity, 'total': product.price * quantity})
                total += product.price * quantity
        return render(request, self.template_name, {'cart_items': cart_items, 'total': total})

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('remove_product_id')
        if product_id:
            cart = request.session.get('cart', {})
            if product_id in cart:
                del cart[product_id]
                request.session['cart'] = cart
                messages.success(request, "Item removed from cart!")
            return redirect('cart')
        return self.get(request, *args, **kwargs)


class CheckoutView(View):
    template_name = 'menus/checkout.html'
