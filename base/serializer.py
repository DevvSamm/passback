from rest_framework import routers, serializers, viewsets
from .models import Hotel, Forfait


class HotelSerializer(serializers.ModelSerializer):
    # galerie = serializers.StringRelatedField(many=True)
    class Meta:
        model = Hotel
        fields = ['name','contact','contact2','cover', 'lng', 'lat','wifi','piscine','parking','climatisation','galerie','forfaits']
        depth=1

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


# FORFAIT
class ForfaitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Forfait
        fields = ['hotel','prix','type']

class ForfaitViewSet(viewsets.ModelViewSet):
    queryset = Forfait.objects.all()
    serializer_class = ForfaitSerializer

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('forfait', ForfaitViewSet)