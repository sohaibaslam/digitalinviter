from django.contrib import admin

from event.models import Event, EventTimeline, EventHost, ThemeImage, Invitation


class EventTimelineAdmin(admin.TabularInline):
    model = EventTimeline


class EventHostAdmin(admin.TabularInline):
    model = EventHost


class EventAdmin(admin.ModelAdmin):
    model = Event
    inlines = [
        EventTimelineAdmin,
        EventHostAdmin
    ]


class ThemeImageAdmin(admin.ModelAdmin):
    model = ThemeImage


class InvitationAdmin(admin.ModelAdmin):
    model = Invitation


admin.site.register(Event, EventAdmin)
admin.site.register(ThemeImage, ThemeImageAdmin)
admin.site.register(Invitation, InvitationAdmin)
