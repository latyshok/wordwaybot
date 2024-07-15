from django.contrib import admin

from telegrambot.models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'telegram_id',
        'is_premium',
        'chat_member_status',
        'added_to_attachment_menu',
        'language_code',
    ]
