from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Boundary


class BoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Boundary
        geo_field = "mpoly"
        fields = "__all__"
