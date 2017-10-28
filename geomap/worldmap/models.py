from django.contrib.gis.db import models

# Create your models here.

class GeoBorder(models.Model):
    """модель географических данных"""
    name = models.CharField(max_length=80)
    area = models.IntegerField()
    pop2005 = models.IntegerField("Population 2005")
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    polygon_map = models.MultiPolygonField()

    def __str__(self):
        return self.name
