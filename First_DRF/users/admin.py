from django.contrib import admin
from django.db.models import Q

from .models import News, Category, User


@admin.register(News)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)