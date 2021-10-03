from django.contrib import admin
from lewagon.models import Update

class UpdateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Update, UpdateAdmin)
