from django.db import models
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError

def validateScale1to10(value):
    if value > 10 or value < 0:
        raise ValidationError(u'%s is not on a scale of 1 to 10' % value)

class Delta (models.Model):
    percentLandChange = models.DecimalField(max_digits=5,decimal_places=2)
    designator = models.CharField(max_length=50)

class Tile (models.Model):
    geotiff = models.FileField()
    designator = models.CharField(max_length=50)
    satellite = models.CharField(max_length=50)
    resolutionInMeters = models.DecimalField(max_digits=5,decimal_places=2)
    region = models.CharField(max_length=50)
    dateTimeOfCapture = models.DateTimeField(auto_now_add=False)
    humanPresenceLevel = models.IntegerField(validators=[validateScale1to10])
    interestLevel = models.IntegerField(validators=[validateScale1to10])
    cloudCoverage = models.DecimalField(max_digits=5,decimal_places=2)
    delta = models.ForeignKey(to=Delta, on_delete=models.CASCADE, null=True)


class Point (models.Model):
    
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    nextPoint = models.ForeignKey('self',null=True,on_delete=models.CASCADE)

class Object (models.Model):
    tile = models.ForeignKey(to=Tile, on_delete=models.CASCADE)

    taggedName = models.CharField(max_length=50)
    predictedName = models.CharField(max_length=50)
    percentOfTile = models.DecimalField(max_digits=5,decimal_places=2)

    firstPoint = models.OneToOneField(
        Point,
        on_delete=models.CASCADE,
    )
