from django.apps import AppConfig


class ModelsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models_app'
    # В админке слева, заголовок над колонкой (Картинки, Пользователи, Лайки etd)
    verbose_name = 'Всякие варики'
