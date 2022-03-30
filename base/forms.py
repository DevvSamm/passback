from dataclasses import field
from django import forms
from .models import Hotel, ImageHotel, Forfait


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ("name", "localisation", "contact", "contact2", "lng", "lat", "cover", "wifi", "climatisation", "piscine", "parking", "place")