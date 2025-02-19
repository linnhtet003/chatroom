from django.contrib import admin
from .models import *

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'joined_date', 'name']
    ordering = ['joined_date', 'email']
    search_fields = ['email', 'name']

admin.site.register(CustomUser, CustomUserAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'host', 'description', 'member_count']
    ordering = ['updated', 'created']
    search_fields = ['name', 'topic__name', 'description']

    def member_count(self, obj):
        return obj.members.count()  # Assuming 'members' is a ManyToManyField

    member_count.short_description = "Members"  # Column name in admin panel

admin.site.register(Room, RoomAdmin)

class TopicAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Topic, TopicAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'room']
    ordering = ['created', 'updated']
    search_fields = ['comment', 'room__name', 'user__email']

admin.site.register(Message, MessageAdmin)