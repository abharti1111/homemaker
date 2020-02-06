from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework import authentication,permissions
from .models import Menu
# Create your views here.

class menuCreateRetrieveUpdateView(generics.CreateAPIView,generics.RetrieveUpdateAPIView):
    serializer_class = MenuSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    lookup_field = 'org'

class organisationCreateView(generics.ListCreateAPIView):
    serializer_class = OrganisationCreateSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Organisation.objects.all()

class organisationUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    serializer_class = OrganisationCreateSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Organisation.objects.all()


