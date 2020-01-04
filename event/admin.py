from django.contrib import admin

from event.models import Event, EventTimeline, EventHost


class EventTimelineAdmin(admin.TabularInline):
    model = EventTimeline


class EventHostAdmin(admin.TabularInline):
    model = EventHost


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventTimelineAdmin,
        EventHostAdmin
    ]


admin.site.register(Event, EventAdmin)
