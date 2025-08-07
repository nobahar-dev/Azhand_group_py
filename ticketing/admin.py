from django.contrib import admin
from .models import *


class TicketReplyInline(admin.TabularInline):
    model = TicketReply
    extra = 1


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'company', 'unit', 'date_created')
    list_filter = ('user', 'date_created', 'status')
    search_fields = ('title', 'description')
    inlines = [TicketReplyInline]
    
    
@admin.register(TicketReply)
class TicketInlineAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'date_created', 'user')