from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Hospital


class HospitalAdmin(LeafletGeoAdmin):
    list_display = ["name", "lon", "lat", "beds", "province_name", "province_code"]


admin.site.register(Hospital, HospitalAdmin)
