from django.contrib import admin
from django.db.models import Q

from .models import News, Category, User


@admin.register(News)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    exclude = ('email', 'user_permissions', 'groups', 'date_joined', 'last_login')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)