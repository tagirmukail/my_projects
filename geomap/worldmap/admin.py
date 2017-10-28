from django.contrib.gis import admin

from .models import GeoBorder

# Register your models here.

admin.site.register(GeoBorder, admin.GeoModelAdmin)
