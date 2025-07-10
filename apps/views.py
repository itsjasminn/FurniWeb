from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from apps.models import Product, ContactInfo
from .forms import MessageForm
from .models import Message


def home_view(request):
    return render(request, 'base/include.html')


def about_view(request):
    return render(request, 'menus/about.html')


def blog_view(request):
    return render(request, 'menus/blog.html')


def cart_view(request):
    return render(request, 'menus/cart.html')


def checkout_view(request):
    return render(request, 'menus/checkout.html')


def index_view(request):
    return render(request, 'menus/index.html')


def services_view(request):
    return render(request, 'menus/services.html')


def shop_view(request):
    data = {"products": Product.objects.all()}
    return render(request, 'menus/shop.html', data)


def thankyou_view(request):
    return render(request, "menus/thankyou.html")


import random
from datetime import timedelta

from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView
from redis import Redis

from apps.forms import EmailForm, LoginModelForm
from apps.models import User
from root.settings import EMAIL_HOST_USER


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
        contact_details = ContactInfo.objects.all()
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
        contact_details = ContactInfo.objects.all()
        return render(request, self.template_name, {'form': form, 'contact_details': contact_details})
