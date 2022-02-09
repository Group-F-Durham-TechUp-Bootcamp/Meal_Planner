from django.contrib import admin

from . import models

class SecurityAdmin(admin.ModelAdmin):
    list_display = {'title',}

admin.site.register(models.Security, SecurityAdmin)
