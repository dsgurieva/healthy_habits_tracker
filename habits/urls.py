from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitsCreateAPIView, HabitsListAPIView, HabitsRetrieveAPIView, HabitsUpdateAPIView, \
    HabitsDestroyAPIView


app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitsListAPIView.as_view(), name='habits_list'),
    path('create/', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits_get'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits_update'),
    path('delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits_delete'),
]
