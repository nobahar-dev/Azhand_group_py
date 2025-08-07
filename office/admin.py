from django.contrib import admin
from .models import *


@admin.register(OfficeArticle)
class OfficeArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'is_published')
    list_filter = ('author', 'date_created', 'is_published')
    
    def has_add_permission(self, request):
        return super().has_add_permission(request)
    
    def has_change_permission(self, request, obj = ...):
        return super().has_change_permission(request, obj)
    
    def has_view_permission(self, request, obj = ...):
        return super().has_view_permission(request, obj)
    
    
@admin.register(OfficeCategory)
class OfficeCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_created', 'date_updated')
    list_filter = ('date_created', 'date_updated')
    
    
@admin.register(OfficeComment)
class OfficeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'date_created')
    list_filter = ('date_created', 'user', 'article')