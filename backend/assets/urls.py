from django.urls import path
from .views import AssetCreateAPIView, UserCreateAPIView, UserClassListAPIView

urlpatterns = [
    path('api/assets/', AssetCreateAPIView.as_view(), name='asset-create'),
    path('api/users/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/user-classes/', UserClassListAPIView.as_view(), name='user-class-list'),
]
