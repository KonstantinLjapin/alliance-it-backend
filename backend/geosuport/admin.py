from django.contrib import admin
from .models import GEO


@admin.register(GEO)
class CustomGeoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'anti')


