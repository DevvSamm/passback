
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from base.models import Hotel
from base.serializer import HotelSerializer

# Create your views here.
def get_hotel(request):

    hotels = Hotel.objects.all()
    hotels_json = HotelSerializer(hotels, many=True)

    return JsonResponse(hotels_json.data, safe=False)

def get_hote(request):
    
    lng = float(request.GET["lng"])
    lat = float(request.GET["lat"])

    list = []
    for obj in Hotel.objects.all():
        if obj.get_proche(lng, lat):
            list.append(obj)
    
    results = HotelSerializer(list, many=True)
    return JsonResponse(results.data, safe=False)