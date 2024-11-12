from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
     class Meta:
         model = Menu
         fields = ['title','price','inventory']
         extra_kwargs = {
            'price':{'min_value':0},
            'inventory':{'min_value':0},
            }
         
class BookingSerializer(serializers.ModelSerializer):
     class Meta:
         model = Booking
         fields = '__all__'
         extra_kwargs = {
            'price':{'min_value':0},
            'inventory':{'min_value':0},
            }