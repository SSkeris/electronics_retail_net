from django.contrib import admin

from network.models import NetworkNode


class NetworkNodeAdmin(admin.ModelAdmin):
    """Настройка админ панели модели 'NetworkNode'."""

    list_display = ('title', 'contact', 'level', 'debt', 'created_at')
    list_filter = ('contact__city',)
    search_fields = ('title', 'contact__city')

    def clear_debt(self, queryset):
        """Убирает задолженность перед поставщиком."""

        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"

    actions = [clear_debt]


admin.site.register(NetworkNode, NetworkNodeAdmin)
