from django.contrib import admin

from greetings.models import Greeting


class GreetingsAdmin(admin.ModelAdmin):
    model = Greeting


admin.site.register(Greeting, GreetingsAdmin)
