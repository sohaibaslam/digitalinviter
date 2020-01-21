from django.contrib import admin

from themes.models import Theme


class ThemeAdmin(admin.ModelAdmin):
    model = Theme


admin.site.register(Theme, ThemeAdmin)
