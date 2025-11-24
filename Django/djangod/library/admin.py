from django.contrib import admin
from .models import User, Book

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'status', 'created_at']
    list_filter = ['status', 'year', 'created_at']
    search_fields = ['title', 'author', 'genre']
    readonly_fields = ['created_at']