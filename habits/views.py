from rest_framework import generics
from habits.models import Habits
from habits.paginators import HabitsPagination
from habits.permissions import IsOwner
from habits.serializer import HabitsSerializer
from rest_framework.permissions import IsAuthenticated


class HabitsListAPIView(generics.ListAPIView):
    """Вывод привычек пользователя"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habits.objects.filter(owner=self.request.user)


class HabitsCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод отдельной привычеки пользователя"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки пользователя"""
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки пользователя"""
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]