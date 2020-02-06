from django.urls import path
from .views import menuCreateRetrieveUpdateView,organisationCreateView,organisationUpdateRetrieveView
urlpatterns = [
    path('<int:org>/menu/',menuCreateRetrieveUpdateView.as_view()),

    path('',organisationCreateView.as_view()),
    path('<int:pk>/',organisationUpdateRetrieveView.as_view()),
]
