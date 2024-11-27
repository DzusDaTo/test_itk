from django.contrib import admin
from .models import BaseStation


class BaseStationAdmin(admin.ModelAdmin):
    list_display = ('ne', 'address', 'coordinates', 'technology', 'status')
    list_filter = ('status', 'technology')
    search_fields = ('ne', 'address')
    ordering = ('-status',)


admin.site.register(BaseStation, BaseStationAdmin)

