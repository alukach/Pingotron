from pingotron.record.models import *
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    inlines = [PlayerScoreInline]

admin.site.register(Player)
#admin.site.register(Game)
admin.site.register(Game, GameAdmin)
