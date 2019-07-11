from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Polygon


class PolygonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polygon
        geo_field = 'geometry'

        fields = ('letter', 'rank', 'color', 'ascii')
