from django.urls import path
from .views import subscriptionCreateView
urlpatterns = [
    path('subscribe/',subscriptionCreateView.as_view()),
]
