from django.contrib import admin

from web_front.models import Profile, Location, Book, Tv, Cinema, Music


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'origins')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location)
admin.site.register(Book)
admin.site.register(Tv)
admin.site.register(Cinema)
admin.site.register(Music)
