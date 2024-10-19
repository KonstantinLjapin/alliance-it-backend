from django.contrib.gis import admin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.GISModelAdmin):
    list_display = ('name', 'location')




