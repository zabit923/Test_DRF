from django.contrib import admin

from .models import Users, Category



@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)