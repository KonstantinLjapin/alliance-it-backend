from rest_framework import serializers
from .models import Fildmap
from django.contrib.gis.geos import Point


class FildmapUploadSerializer(serializers.Serializer):
    """Сериализатор для записи координат в модель бд"""
    lon = serializers.FloatField()
    lat = serializers.FloatField()

    def validate(self, data):
        # TODO написать логику антимеридиана
        data.update({'antimeridian': True})
        location = Point(float(data.get('lon')), float(data.get('lat')))
        data.update({'location': location})
        return data

    def create(self, validated_data):
        return Fildmap.objects.create(**validated_data)


class FildmaploadSerializer(serializers.Serializer):
    """Сериализатор выгрузки  координат из модели бд"""
    class Meta:
        model = Fildmap
        fields = ('id', 'lon', 'lat', 'antimeridian', 'location')