from rest_framework import viewsets

from .models import Polygon
from .serializer import PolygonSerializer


class PolyViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
