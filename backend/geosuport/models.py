from django.contrib.gis.db import models


class Fildmap(models.Model):
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    antimeridian = models.BooleanField(default=False)
    location = models.PointField(null=True, blank=True)
