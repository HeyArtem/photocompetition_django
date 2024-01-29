from django.contrib import admin
from models_app.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = ('id', 'is_answer', 'answer', 'updated_at', 'post', 'user',)

    # Кликабельность в шапке
    list_display_links = ('id', 'is_answer', 'answer', 'post', 'user',)

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ('id', 'is_answer', 'answer', 'updated_at', 'post', 'user',)

    # Справа Фильтр
    list_filter = ('id', 'is_answer', 'answer', 'updated_at', 'user', 'created_at',)

    # Сортирока порядок
    ordering = ('-updated_at', 'is_answer', 'answer')

    # Пагинация
    list_per_page = 3
