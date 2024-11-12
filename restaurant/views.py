from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu,Booking


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price','inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']
    def get_permissions(self):
        if (self.request.method =='POST' ):
            return[IsAdminUser()] 
        return[]
    
        
    #def postitem(self):
     #   if(self.request.method =='POST' ):
      #      return []

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get_permissions(self):
        if(self.request.method == 'GET'):
            return[]
        if(self.request.method =='DELETE','POST','PATCH' ):
            return [IsAdminUser()]
        return[]
    
class BookingView(viewsets.ModelViewSet):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        permission_classes = [IsAuthenticated]
        