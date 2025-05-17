from django.contrib import admin
from .models import QueryHistory

# Register your models here.

class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_query', 'created_at')

    def short_query(self, obj):
        return obj.query[:50] + ('...' if len(obj.query) > 50 else '')