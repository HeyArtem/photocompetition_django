from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from models_app.models import User
from django.db.models import QuerySet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = (
        'id', 'username',  'first_name', 'last_name', 'get_html_avatar', 'date_joined', 'is_staff', 'is_active',)

    # TODO:Почему не раб?
    # list_display = ('__str__', 'some_other_field')

    # Кликабельность в шапке
    list_display_links = ('id', 'username', 'get_html_avatar')

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ('username', 'email', 'first_name')

    # Справа Фильтр
    list_filter = ('username', 'first_name', 'is_staff', 'date_joined')

    # Возможность отредачить мышкой (is_staff/is NOT staff)
    list_editable = ('is_staff', 'is_active')

    # Сортирока порядок
    ordering = ('-date_joined', 'username')

    # # Какие поля отображать (исключить в админке). Я не могу найти последний вход
    # # fields = ()
    # exclude = ('email', 'last_login')

    # Блоки в админке
    fieldsets = [
        ("Общая информация", {'fields': ['username', 'password', 'avatar', ]}),
        ('Права доступа', {'fields': ['is_superuser', 'is_staff', 'is_active']}),
        ('Прочая информация',
         {'fields': ['last_login', 'date_joined', 'first_name', 'last_name',]}),
    ]

    # Запрещенные, при редактировании поля
    readonly_fields = ('date_joined',)

    # Пагинация
    list_per_page = 3

    # Отображение аватара-картинки
    def get_html_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width=50>')
        return ' - '

    # Подпись в шапке 'Аватар' (не get_html_avatar )
    get_html_avatar.short_description = 'Аватар'

    # Регистрация метода set_is_active(Изменить статус АКТИВНЫЙ)
    actions = ('set_is_active',)

    # Раздел 'Действие' фун-я активный/НЕ активный для ВСЕХ
    @admin.action(description='Изменить статус АКТИВНЫЙ')
    def set_is_active(self, request, qs: QuerySet):
        count_updated = qs.update(is_active=True)

        # Сообщение юзеру, сколько произведено изменений
        self.message_user(
            request,
            f"Было изменено {count_updated} записей",
            # Дизайн вывода сообщения
            messages.SUCCESS
        )
