from django.contrib import admin
from .models import Stok, TransaksiStok

@admin.register(Stok)
class StokAdmin(admin.ModelAdmin):
    list_display = ('barang', 'jumlah', 'gudang')
    readonly_fields = ('jumlah',) # Agar jumlah tidak bisa diedit sembarangan (harus lewat transaksi)

@admin.register(TransaksiStok)
class TransaksiStokAdmin(admin.ModelAdmin):
    list_display = ('barang', 'tipe', 'jumlah', 'tanggal')