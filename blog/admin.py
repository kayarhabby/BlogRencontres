from django.contrib import admin

# Register your models here.

from .models import Blog, Comments, Contact, Team, Gallery


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
   # prepopulated_fields = {'title': ('title',)}
    ordering = ('-created_at',)

admin.site.register(Blog, BlogAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'created_at')
    search_fields = ('blog__title', 'name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
admin.site.register(Comments, CommentsAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
admin.site.register(Contact, ContactAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Team, TeamAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at')
    search_fields = ('image',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
admin.site.register(Gallery, GalleryAdmin)