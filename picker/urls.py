from django.urls import path, include
from .views import GetColourAPIView

urlpatterns = [
    path('findColours/', GetColourAPIView.as_view())
]