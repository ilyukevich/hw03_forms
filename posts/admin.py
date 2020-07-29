from django.contrib import admin
from .models import Post
from .models import Group

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    # добавим в начало столбец pk
    list_display = ("pk", "text", "pub_date", "author")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    """Group fields that are displayed in the admin panel"""
    list_display = ("title", "slug", "description")
    search_fields = ()
    list_filter = ()
    empty_value_display = "-пусто-"

# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)