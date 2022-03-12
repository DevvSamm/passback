from pyexpat import model
from rest_framework import routers, serializers, viewsets
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name','contact', 'lng', 'lat']

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializers = HotelSerializer

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet)