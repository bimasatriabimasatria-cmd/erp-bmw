from django.contrib import admin
from .models import Kategori, Satuan, Barang

# Mendaftarkan tabel agar muncul di layar visual
admin.site.register(Kategori)
admin.site.register(Satuan)
admin.site.register(Barang)