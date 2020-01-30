from django.urls import path
from .views import userRegisterAPIView,ObtainAuthToken,profileCreationView,profileUpdateRetrieveView

urlpatterns = [
    path('register/',userRegisterAPIView.as_view(),name='register'),
    path('obtain_auth_token/',ObtainAuthToken.as_view(),name='obtain_auth_token'),
    path('create_profile/',profileCreationView.as_view(),name='create_profile'),
    path('update_profile/<int:user>/',profileUpdateRetrieveView.as_view(),name='update_profile'),
]
