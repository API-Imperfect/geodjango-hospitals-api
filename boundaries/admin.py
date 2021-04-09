from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Boundary


class BoundaryAdmin(LeafletGeoAdmin):
    list_display = ["pk", "name", "pcode"]

    list_display_links = ["name"]


admin.site.register(Boundary, BoundaryAdmin)
