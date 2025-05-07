from django.conf import settings
from django.utils.translation import gettext as _

import telebot
from telebot import types

from bot.utils import get_sub_from_message
from bot.models import Subscriber

bot = telebot.TeleBot(settings.BOT_API_KEY)


def send_message_to_subscribers(message):
    subscribers = Subscriber.objects.filter(is_active=True)
    for subscriber in subscribers:
        bot.send_message(subscriber.chat_id, message)


def create_keyboard():
    """Создает клавиатуру с кнопками подписки и отписки."""
    keyboard = types.InlineKeyboardMarkup()
    subscribe_button = types.InlineKeyboardButton(
        _("Подписаться"), callback_data='subscribe')
    unsubscribe_button = types.InlineKeyboardButton(
        _("Отписаться"), callback_data='unsubscribe')

    keyboard.add(subscribe_button, unsubscribe_button)

    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    """Отправляет сообщение при команде /start."""
    bot.reply_to(
        message,
        _("Привет! Я бот отслеживающий входы в Django-admin. Вы можете подписаться и отписаться от уведомлений."),
    )
    bot.send_message(message.chat.id, _("Выберите опцию:"),
                     reply_markup=create_keyboard())


def subscribe(message) -> bool:
    sub = get_sub_from_message(message)

    if sub and sub.is_active:
        return False
    elif sub and not sub.is_active:
        sub.activate()
        return True
    else:
        Subscriber.objects.create(
            chat_id=message.from_user.id,
        )
        return True


def unsubscribe(message) -> bool:
    sub = get_sub_from_message(message)

    if sub and sub.is_active:
        sub.deactivate()
        return True
    else:
        return False


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    """Обрабатывает нажатия кнопок в меню Бота."""
    ans = _('Неизвестная команда!')

    if call.data == 'subscribe':
        res = subscribe(call)
        if res:
            ans = _("Вы подписались на сообщения!")
        else:
            ans = _("Вы уже подписанны на сообщения!")

    elif call.data == 'unsubscribe':
        res = unsubscribe(call)
        if res:
            ans = _("Вы отписались от сообщений!")
        else:
            ans = _("Вы не подписанны на сообщения!")

    bot.send_message(call.from_user.id, ans)
    bot.send_message(call.from_user.id, _("Выберите опцию:"),
                     reply_markup=create_keyboard())


def start_bot():
    bot.polling(none_stop=True)
