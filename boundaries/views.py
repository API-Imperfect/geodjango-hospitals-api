from rest_framework import viewsets

from .models import Boundary
from .serializers import BoundarySerializer


class BoundaryViewset(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
