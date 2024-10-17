from django.db import models


class GEO(models.Model):
    title = models.CharField(max_length=255)
    anti = models.BooleanField(default=False)

    def __str__(self):
        return "GEO " + str(self.title)
