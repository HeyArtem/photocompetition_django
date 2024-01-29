from django.contrib import admin
from models_app.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    # Подписи в шапке
    list_display = ('id', 'state',)

    # Кликабельность в шапке
    list_display_links = ('id', 'state',)

