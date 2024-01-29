from django.contrib import admin

from models_app.admin.like.admin import LikeInline
from models_app.admin.picture.admin import PictureInline
from models_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = ('id', 'status', 'title', 'updated_at', 'user',)

    # Кликабельность в шапке (нельзя одновременно с list_editable)
    list_display_links = ('id', 'title', 'user',)

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ('id', 'status', 'title', 'updated_at', 'user',)

    # Справа Фильтр
    list_filter = ('status', 'user',)

    # Возможность отредачить мышкой (is_staff/is NOT staff)
    list_editable = ('status',)

    # Сортирока порядок
    ordering = ('-updated_at', 'status', 'user',)

    # Пагинация
    list_per_page = 25

    # Автоматич-е заполнение slug
    prepopulated_fields = {"slug": ("title",)}

    # при заполнении удобно выводятся все авторы
    raw_id_fields = ['user']

    # сверху строка навигации по датам
    date_hierarchy = 'updated_at'

    inlines = (PictureInline, LikeInline)
    readonly_fields = ('created_at', 'count_likes', 'updated_at', 'id')

    fieldsets = [
        ("Общая информация", {'fields': ['id', 'title', 'slug', 'status', 'user', ]}),
        ('Прочая информация',
         {'fields': ['count_likes', 'description', 'updated_at', 'created_at', ]}),
    ]

    def count_likes(self, obj):
        return obj.likes_post.all().count()

    count_likes.short_description = 'Кол-во лайков'
