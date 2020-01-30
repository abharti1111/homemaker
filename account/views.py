from django.shortcuts import render
from .serializers import userCreateSerializer,authTokenSerializer,userProfileUpdateSerializer
from rest_framework import generics
from rest_framework import permissions,authentication
from django.contrib.auth.models import User
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

class userRegisterAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = userCreateSerializer

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = authTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class profileCreationView(generics.CreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset=Profile.objects.all()
    serializer_class = userProfileUpdateSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
class profileUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_classes=[IsOwnerOrReadOnly,permissions.IsAuthenticatedOrReadOnly]
    queryset=Profile.objects.all()
    serializer_class = userProfileUpdateSerializer
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'user'

class profileCreateAddressView(generics.CreateAPIView):
    pass


    

    

