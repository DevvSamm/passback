from os import environ
from statistics import mode
from tokenize import blank_re
from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    localisation = PlainLocationField(based_fields = ['city'], zoom=7, blank=True)
    contact = models.CharField(max_length=20)
    lng = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)
    #photo
    #galerie
    #contact2
    #forfait
        #prix
        #

    
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