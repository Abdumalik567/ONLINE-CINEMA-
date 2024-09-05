# users/admin.py
from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    # Определите поля, которые вы хотите отображать в списке
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Определите поля, которые можно фильтровать
    list_filter = ('is_staff', 'is_active')
    # Определите поля для поиска
    search_fields = ('username', 'email')
    # Определите порядок сортировки
    ordering = ('username',)

    # Настройте поля на странице редактирования
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Настройте поля при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
