
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GEOSerializer
from .models import GEO


class GEOView(GenericAPIView):
    serializer_class = GEOSerializer





