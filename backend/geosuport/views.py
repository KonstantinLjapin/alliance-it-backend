from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import FildmapUploadSerializer, FildmaploadSerializer

from .models import Fildmap


class AddFildmapview(APIView):
    """Вью для загрузки кооординат"""
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = FildmapUploadSerializer

    def post(self, request):
        bike_serializer = FildmapUploadSerializer(data=request.data)
        bike_serializer.is_valid()
        bike_serializer.save()
        return Response({'message': 'data_write'}, status=status.HTTP_200_OK)


class FildmapListview(APIView):
    """Вью для выгрузки кооординат"""
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = FildmaploadSerializer

    def get(self, request):
        # TODO понять почему ответ не сериализируется
        fm = Fildmap.objects.all()
        serializer = FildmaploadSerializer(instance=fm, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

