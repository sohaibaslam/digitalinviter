from django.contrib import admin

from rsvp.models import RSVP


class RSVPAdmin(admin.ModelAdmin):
    model = RSVP


admin.site.register(RSVP, RSVPAdmin)
