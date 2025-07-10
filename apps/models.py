from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import Model, TextField, CharField, ImageField, DecimalField, DateField, ForeignKey, \
    PositiveIntegerField, CASCADE
from django.db.models.fields import SmallIntegerField, EmailField, DateTimeField


class CustomerUser(UserManager):
    def _create_user_object(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        user = self._create_user_object(email, password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = EmailField(max_length=255, unique=True)
    image = ImageField(upload_to='profile_photos', null=True, blank=True)
    phone_number = CharField(max_length=25, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomerUser()


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(null=True, blank=True)
    quantity = SmallIntegerField(default=1)
    image = ImageField(upload_to='products/')
    created_at = DateField(auto_now=True)


class Message(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(max_length=255)
    message = TextField()
    created_at = DateField(auto_now=True)

    def write(self):
        try:
            self.full_clean()
            self.save()
            return True
        except ValidationError:
            return False


class ContactDetails(Model):
    address = CharField(max_length=255)
    email = EmailField(max_length=255)
    phone = CharField(max_length=20)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class TeamMember(Model):
    name = CharField(max_length=100)
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='team_images/', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CartItem(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    added_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
