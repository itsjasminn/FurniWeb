from django.db.models import Model, TextField, CharField, ImageField, DecimalField, DateField
from django.db.models.fields import SmallIntegerField


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(null=True, blank=True)
    quantity = SmallIntegerField(default=1)
    image = ImageField(upload_to='products/')
    created_at = DateField(auto_now=True)


