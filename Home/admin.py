from django.contrib import admin
from .models import Contact, Blog


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'read_time']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)