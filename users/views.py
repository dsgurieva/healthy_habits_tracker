from rest_framework import generics
from users.models import User
from users.serializer import UserSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny


class UserCreateAPIView(generics.ListCreateAPIView):
    """Создание пользователя"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(generics.DestroyAPIView):
    """Удаление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer