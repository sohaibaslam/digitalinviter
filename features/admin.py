from django.contrib import admin

from features.models import Feature


class FeatureAdmin(admin.ModelAdmin):
    model = Feature


admin.site.register(Feature, FeatureAdmin)
