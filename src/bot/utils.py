from bot.models import Subscriber


def get_sub_from_message(message) -> Subscriber | None:
    chat_id = message.from_user.id
    try:
        sub = Subscriber.objects.get(chat_id=chat_id)
    except Subscriber.DoesNotExist:
        sub = None
    return sub
