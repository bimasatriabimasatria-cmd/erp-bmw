from django.contrib import admin
from .models import ResepProduksi, KomponenResep, WorkOrder

# Ini adalah 'Inline' - membuat form Komponen muncul di bawah Resep
class KomponenResepInline(admin.TabularInline):
    model = KomponenResep
    extra = 1  # Menampilkan 1 baris kosong untuk tambah bahan baru secara default

@admin.register(ResepProduksi)
class ResepProduksiAdmin(admin.ModelAdmin):
    inlines = [KomponenResepInline] # Menggabungkan form komponen ke sini
    list_display = ('nama_resep', 'produk_hasil', 'jumlah_hasil')

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('nomor_wo', 'resep', 'target_produksi', 'status')
    list_filter = ('status',)

admin.site.register(KomponenResep) # Masih tetap didaftarkan agar bisa dikelola mandiri jika perlu