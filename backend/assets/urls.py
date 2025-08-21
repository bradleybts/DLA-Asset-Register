from django.urls import path
from .views import AssetCreateAPIView, UserCreateAPIView, UserClassListAPIView

urlpatterns = [
    path('assets/', AssetCreateAPIView.as_view(), name='asset-create'),
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('user-classes/', UserClassListAPIView.as_view(), name='user-class-list'),
]
