from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def create_user(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('1234')
        self.user.save()

    def setUp(self) -> None:
        """Подготовка данных"""
        self.create_user()

        self.habits = Habits.objects.create(
            action="habits test",
            periodicity="1",
            limit_time="10"
        )

    def test_list_habits(self):
        """Тестирование вывода привычки"""

        response = self.client.get(
            reverse('habits:habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "location": null,
                "time": null,
                "action": "habits test",
                "good_habit": false,
                "periodicity": 1,
                "award": null,
                "limit_time": 10,
                "public": false,
                "owner": 2,
                "habit_link": null
            }
        )

    def test_update_habits(self):
        """Тестирование обновления привычек"""
        self.client.force_authenticate(self.user)
        data = {
            'action': 'test habits updated',
        }

        response = self.client.patch(
            reverse("habits:habits_update", kwargs={'pk': self.habits.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habits.objects.get(pk=self.habits.id).action,
            'test habits updated'
        )

    def test_delete_habits(self):
        """Тестирование удаления привычек"""
        self.client.force_authenticate(self.user)
        response = self.client.delete(
            reverse("habits:habits_delete", kwargs={'pk': self.habits.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Habits.objects.exists()
        )