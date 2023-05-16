from typing import Optional, Type
from django.contrib import admin
from datetime import datetime

from django.contrib.admin.sites import AdminSite

from .models import Account, Article
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "surname"]

    search_fields = [
        "name",
        "surname",
    ]

class ArticleAdmin(admin.ModelAdmin):
    
    def __init__(self, model: type, admin_site: AdminSite) -> None:
        super().__init__(model, admin_site)
        self.list_display = ["id", "title", "author", "published"]

        self.search_fields = [
            "title",
            "author__name",
            "author__surname",
        ]

        self.actions = [self.clear_content, self.clear_datetime]

    @admin.display(description="Clear Content Fields")
    def clear_content(self, modeladmin, request, queryset):
        queryset.update(content="")

    @admin.display(description="Reset DateTime Fields")
    def clear_datetime(self, modeladmin, request, queryset):
        queryset.update(published=datetime.now())

admin.site.register(Account)
admin.site.register(Article, ArticleAdmin)