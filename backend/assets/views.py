from rest_framework import generics
from .models import Asset, CustomUser, UserClass
from .serializers import AssetSerializer, UserSerializer, UserClassSerializer

class AssetCreateAPIView(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserClassListAPIView(generics.ListAPIView):
    queryset = UserClass.objects.all()
    serializer_class = UserClassSerializer
