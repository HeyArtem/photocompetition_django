from django.contrib import admin
from models_app.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = ('id', 'user', 'post')

    # Кликабельность в шапке
    list_display_links = ('user', 'post')

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ('user', 'post')

    # Справа Фильтр
    list_filter = ('user', 'post')

    # Сортирока порядок
    ordering = ('post',)


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
