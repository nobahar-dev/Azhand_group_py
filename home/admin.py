from django.contrib import admin
from .models import *


@admin.register(Modal)
class ModalAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')