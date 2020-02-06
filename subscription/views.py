from django.shortcuts import render
from .serializers import subscriptionSerializer
from rest_framework import generics,authentication,permissions
from .models import Booking
# Create your views here.

class subscriptionCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = subscriptionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]