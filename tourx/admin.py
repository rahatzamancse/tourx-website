from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tourx import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from tourx.models import Profile


@admin.register(Profile)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Files'), {'fields': ('profile_pic', 'photo_id')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


# admin.register(models.Profile)(admin.ModelAdmin)
admin.register(models.Place)(admin.ModelAdmin)
admin.register(models.Counter)(admin.ModelAdmin)
admin.register(models.Review)(admin.ModelAdmin)
