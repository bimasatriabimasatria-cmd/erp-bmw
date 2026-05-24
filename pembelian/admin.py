from django.contrib import admin
from .models import PurchaseOrder, PurchaseItem

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [PurchaseItemInline]
    list_display = ('nomor_po', 'supplier', 'status')