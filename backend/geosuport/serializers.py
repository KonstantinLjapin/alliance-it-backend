from rest_framework import serializers
from .models import Fildmap
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class FildmapUploadSerializer(serializers.Serializer):
    """Сериализатор для записи координат в модель бд"""
    lon = serializers.FloatField()
    lat = serializers.FloatField()

    def validate(self, data):
        #
        data.update({'antimeridian': True})
        location = Point(float(data.get('lon')), float(data.get('lat')))
        data.update({'location': location})
        return data

    def create(self, validated_data):
        return Fildmap.objects.create(**validated_data)


class FildmaploadSerializer(GeoFeatureModelSerializer):
    """Сериализатор выгрузки  координат из модели бд в формате geo json rfc7946"""
    class Meta:
        model = Fildmap
        geo_field = 'location'
        fields = ('id', 'lon', 'lat', 'antimeridian')
