from django.core.management.base import BaseCommand
from bot.bot import start_bot


class Command(BaseCommand):
    help = 'Запускает TG-бота'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Запуск бота...'))
        start_bot()
        self.stdout.write(self.style.SUCCESS('Бот запущен!'))
