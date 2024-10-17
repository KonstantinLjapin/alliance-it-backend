from rest_framework import serializers
from .models import GEO


class GEOSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = GEO
        fields = ('id', 'title', 'poly', 'anti')

