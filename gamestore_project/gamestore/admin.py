from django.contrib import admin

from gamestore.models import Platform, Game, UserProfile

# Register your models here.

admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(UserProfile)