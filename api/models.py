from django.contrib.gis.db import models


class Polygon(models.Model):
    letter = models.CharField(max_length=1)
    color = models.CharField(max_length=13)
    rank = models.IntegerField()
    ascii = models.IntegerField()
    geometry = models.PolygonField()

    def __str__(self):
        return self.letter + ' ' + self.color
