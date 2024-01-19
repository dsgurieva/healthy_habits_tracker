from django.db import models
from config import settings


class Habits(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True, verbose_name='место выполнения')
    time = models.DateTimeField(null=True, blank=True, verbose_name='дата выполнения')
    action = models.CharField(max_length=500, verbose_name='действие')
    good_habit = models.BooleanField(default=False, verbose_name='признак приятной привыки')
    habit_link = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связвнная привычка', null=True,
                                   blank=True)
    periodicity = models.SmallIntegerField(verbose_name='периодичность - (количество повторений в неделю)')
    award = models.CharField(max_length=100, verbose_name='награда', null=True, blank=True)
    limit_time = models.SmallIntegerField(verbose_name='продолжительность')
    public = models.BooleanField(default=False, verbose_name='признак публичность')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'