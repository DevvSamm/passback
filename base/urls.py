from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_hotel),
    path('get_hote/', views.get_hote)
]