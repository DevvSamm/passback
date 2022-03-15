from distutils.command.upload import upload
from email.policy import default
from os import environ
from statistics import mode
from tokenize import blank_re
from django.db import models
from location_field.models.plain import PlainLocationField
from places.fields import PlacesField
import uuid


def upload_directory(instance, filename):
    return f"galerie/{instance.id}/"


class Hotel(models.Model):
    identifiant = models.UUIDField('identifiant', default=uuid.uuid4, editable=False)
    valide = models.BooleanField(default=False)


    name = models.CharField("nom de l'hotel",max_length=200)
    localisation = PlainLocationField(based_fields = ['city'], zoom=7, blank=True)
    contact = models.CharField(max_length=20)
    contact2 = models.CharField(max_length=20, blank=True)
    lng = models.FloatField("longitude",blank=True)
    lat = models.FloatField("latitude",blank=True)
    cover = models.ImageField("image de couverture",upload_to = "cover/", default='hotel_placeholder.png')
    wifi = models.BooleanField(default=False)
    climatisation = models.BooleanField(default=False)
    piscine = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    place = PlacesField(blank=True, null=True)
    

    def environant(self, v:float, ecart=0.001):
        """
            renvoie le plus et le moin
            prends une position en particulier et retourne le plus et le moin
        """
        moins = v - ecart
        plus =  v + ecart
        return (moins, plus)
    
    def get_proche(self, x, y):
        """
            estime si l'hotel est compris dans les environs des coordonnées selectionnée
        """
        x_moins, x_plus = self.environant(x)
        y_moins, y_plus = self.environant(y)


        # A resourdre  avec numpy
        # if self.lng in range(x_moins, x_plus) and self.lat in range(y_moins, y_plus):
        #     return True

        if (self.lng > x_moins and self.lng < x_plus) and (self.lat > y_moins and self.lat < y_plus):
            return True
        
        return False


    def __str__(self) -> str:
        return self.name

class ImageHotel(models.Model):
    image = models.ImageField("image", upload_to=upload_directory)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='galerie')

    def __str__(self) -> str:
        return self.image.url


class Forfait(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='forfaits')
    TYPE_FORFAIT = (
        ('passage', 'passage'),
        ('nuitee', 'nuitee'),
        ('sejour','sejour')
    )
    type = models.CharField( 'type de forfait', max_length=30, choices=TYPE_FORFAIT, default=TYPE_FORFAIT[0][0])
    prix = models.IntegerField()

