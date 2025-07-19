from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

from django.core.cache import cache
from django.http import HttpResponse
import time

def cache_test(request):
    # Try to get value from cache
    value = cache.get('my_key')
    if value is None:
        # Simulate a slow calculation
        time.sleep(3)
        value = "This is cached data!"
        cache.set('my_key', value, timeout=30)  # cache for 30 seconds
        return HttpResponse(f"Cache miss! Value set to: {value}")
    else:
        return HttpResponse(f"Cache hit! Value: {value}")


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class OrderListCreateView(APIView):
    permission_classes = [IsAuthenticated]

# users/views.py
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        if 'password' not in serializer.validated_data:
            raise serializers.ValidationError({"password": "This field is required."})
        serializer.save()
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user