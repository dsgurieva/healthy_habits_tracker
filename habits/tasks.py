from datetime import datetime, timedelta
from celery import shared_task
from habits.models import Habits
from habits.services import send_message, get_updates, parse_updates
from users.models import User


@shared_task
def get_message_data():
    """Отправка сообщения в телеграм"""
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)
    habits = Habits.objects.filter(time__gte=start_time).filter(time__lte=finish_time)

    for habit in habits:
        updates = get_updates()
        if updates['ok']:
            parse_updates(updates['result'])
        chat_id = User.objects.get(telegram=habit.owner.telegram).chat_id
        text = f'Сегодня вам необходимо выполнить {habit.action} в {habit.time}. Место выполнения: {habit.location}'
        send_message(text, chat_id)

        habit.time += timedelta(days=habit.periodicity)
        habit.save()