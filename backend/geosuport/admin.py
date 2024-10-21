from django.contrib.gis import admin
from .models import Fildmap


@admin.register(Fildmap)
class ShopAdmin(admin.GISModelAdmin):
    list_display = ('antimeridian', 'location')




