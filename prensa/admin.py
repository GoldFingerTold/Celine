from django.contrib import admin
from . models import Prensa, imagePrensa

# Register your models here.

class imagePrensaAdmin(admin.TabularInline):
    model = imagePrensa

class PrensaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    inlines = [
        imagePrensaAdmin
    ]

admin.site.register(Prensa, PrensaAdmin)

