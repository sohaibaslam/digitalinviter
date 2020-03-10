from django.contrib import admin

from gallery.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery


admin.site.register(Gallery, GalleryAdmin)
