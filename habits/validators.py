from rest_framework.validators import ValidationError
from habits.models import Habits


class LinkedAndAwardValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_link_valid = dict(value).get('habit_link')
        award_valid = dict(value).get('award')
        if habit_link_valid and award_valid:
            raise ValidationError(
                'Вы не можете выбрать связанную '
                'привычку и вознаграждение одновременно.'
            )


class TimeAwardValidator:

    def __init__(self, limit_time):
        self.limit_time = limit_time

    def __call__(self, value):
        limit_time_valid = dict(value).get(self.limit_time)

        if isinstance(limit_time_valid, int) and limit_time_valid > 120:
            raise ValidationError(
                'Время выполнения должно составлять не более 120 секунд.'
            )


class LinkedHabitIsGoodValidator:

    def __init__(self, habit_link):
        self.habit_link = habit_link

    def __call__(self, value):
        habit_link_valid = dict(value).get(self.habit_link)

        if habit_link_valid:
            habit = Habits.objects.get(pk=habit_link_valid.id)
            if not habit.good_habit:
                raise ValidationError(
                    'В связанные привычки могут попадать только'
                    ' привычки с признаком приятной привычки.'
                )


class GoodHabitValidator:

    def __init__(self, good_habit, habit_link, award):
        self.good_habit = good_habit
        self.habit_link = habit_link
        self.award = award

    def __call__(self, value):
        good_habit_valid = dict(value).get(self.good_habit)
        habit_link_valid = dict(value).get(self.habit_link)
        award_valid = dict(value).get(self.award)

        if (good_habit_valid
                and habit_link_valid
                or good_habit_valid
                and award_valid):
            raise ValidationError(
                'У приятной привычки не может быть '
                'вознаграждения или связанной привычки.'
            )


class HabitPeriodValidator:

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        periodicity_valid = dict(value).get(self.periodicity)

        if isinstance(periodicity_valid, int) and periodicity_valid < 7:
            raise ValidationError(
                'Вы не можете выполнять эту '
                'привычку реже одного раза в 7 дней.'
            )
