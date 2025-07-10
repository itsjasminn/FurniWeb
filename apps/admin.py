from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils import html

from apps.models import Product

admin.site.site_header = "Lumi"
admin.site.site_title = "Lumi's Admin Portal"
admin.site.index_title = "Welcome"

admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'image', 'name', 'quantity', 'is_quantity'

    def is_quantity(self, obj):
        if obj.quantity > 0:
            return html.format_html(
                '<img width="30" height="30" src="https://img.icons8.com/color/30/checked--v1.png" alt="checked--v1"/>')
        else:
            return html.format_html(
                '<img width="30" height="30" src="https://img.icons8.com/emoji/30/cross-mark-button-emoji.png" alt="cross-mark-button-emoji"/>')
