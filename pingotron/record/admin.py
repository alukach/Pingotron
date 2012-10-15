from pingotron.record.models import *
from django.contrib import admin

class PlayerProfileInline(admin.StackedInline):
    model = PlayerProfile

class UserAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    ('Basics',              {'fields': ['Usernametitle', 'eventid', 'category', 'venue']}),
    #    ('Optional',        {'fields': ['slug', 'description', 'time', 'contact', 'cost', 'staffpick', 'buytix']}),
    #]
    inlines = [PlayerProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(PlayerProfile)
admin.site.register(Game)
