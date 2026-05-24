from django.db import models
from master_data.models import Barang

# 1. Resep Utama (Bill of Materials)
class ResepProduksi(models.Model):
    nama_resep = models.CharField(max_length=200, help_text="Contoh: Resep Kain Greige Katun 30s")
    # Produk hasil ini mengambil dari master_data
    produk_hasil = models.ForeignKey(Barang, on_delete=models.CASCADE, related_name='resep_hasil')
    jumlah_hasil = models.DecimalField(max_digits=10, decimal_places=2, help_text="Jumlah target (misal: 1000)")
    
    def __str__(self):
        return self.nama_resep

# 2. Bahan-Bahan dalam Resep (Komponen)
class KomponenResep(models.Model):
    resep = models.ForeignKey(ResepProduksi, on_delete=models.CASCADE)
    bahan_baku = models.ForeignKey(Barang, on_delete=models.RESTRICT, related_name='resep_bahan')
    jumlah_dibutuhkan = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bahan_baku.nama_barang} - {self.jumlah_dibutuhkan}"

# 3. Surat Perintah Kerja (Work Order)
class WorkOrder(models.Model):
    STATUS_PILIHAN = [
        ('DRAFT', 'Draft'),
        ('PROSES', 'Sedang Diproses'),
        ('SELESAI', 'Selesai'),
        ('BATAL', 'Dibatalkan'),
    ]
    
    nomor_wo = models.CharField(max_length=50, unique=True, help_text="Contoh: WO-2026-001")
    resep = models.ForeignKey(ResepProduksi, on_delete=models.RESTRICT)
    target_produksi = models.DecimalField(max_digits=10, decimal_places=2, help_text="Jumlah yang ingin diproduksi")
    status = models.CharField(max_length=20, choices=STATUS_PILIHAN, default='DRAFT')
    is_processed = models.BooleanField(default=False)
    tanggal_mulai = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"[{self.nomor_wo}] {self.resep.produk_hasil.nama_barang}"