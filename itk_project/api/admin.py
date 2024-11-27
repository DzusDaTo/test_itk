from django.contrib import admin
from .models import BaseStation


class BaseStationAdmin(admin.ModelAdmin):
    list_display = ('ne', 'address', 'coordinates', 'technology', 'status')  # Указываем поля для отображения в списке
    list_filter = ('status', 'technology')  # Добавляем фильтрацию по этим полям
    search_fields = ('ne', 'address')  # Указываем поля для поиска
    ordering = ('-status',)  # Сортировка по статусу по убыванию


# Регистрируем модель и настраиваем её отображение в админке
admin.site.register(BaseStation, BaseStationAdmin)

