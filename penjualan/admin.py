from django.contrib import admin
from .models import SalesOrder, SalesItem

class SalesItemInline(admin.TabularInline):
    model = SalesItem
    extra = 1

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    inlines = [SalesItemInline]
    list_display = ('nomor_so', 'pelanggan', 'status')