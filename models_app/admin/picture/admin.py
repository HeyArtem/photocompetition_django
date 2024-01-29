from django.contrib import admin
from django.utils.safestring import mark_safe

from models_app.models import Picture

'''
Весь пост выводить не нужно
Можно  вывести нужно достать из '''


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = ('id', 'current', 'post', 'get_html_image')

    # Кликабельность в шапке
    list_display_links = ('id', 'post', 'current',)

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ('id', 'post', 'current',)

    # Справа Фильтр
    list_filter = ('id', 'current', 'post',)

    # Сортирока порядок
    ordering = ('-post',)

    # Отображение аватара-картинки
    def get_html_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')
        return ' - '

    # Подпись в шапке 'Картинка' (не get_html_avatar )
    get_html_image.short_description = 'Картинка'


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 0
