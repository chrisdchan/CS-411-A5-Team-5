from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'first_name',)
    list_filter = ('email','first_name', 'is_active', 'is_staff', 'promo')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'promo')}),
        ('Personal', {'fields': ('about','goal')})
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'promo', 'goal')}
         ),
    )

admin.site.register(NewUser)
admin.site.register(Patient)
admin.site.register(Training)
admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Audio)
