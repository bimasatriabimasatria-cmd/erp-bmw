from django.db import models
from master_data.models import Barang

class Stok(models.Model):
    barang = models.OneToOneField(Barang, on_delete=models.CASCADE)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gudang = models.CharField(max_length=100, default="Gudang Utama")

    def __str__(self):
        return f"{self.barang.nama_barang}: {self.jumlah}"

class TransaksiStok(models.Model):
    TIPE_TRANSAKSI = [
        ('MASUK', 'Barang Masuk'),
        ('KELUAR', 'Barang Keluar (Produksi)'),
    ]
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)
    tipe = models.CharField(max_length=10, choices=TIPE_TRANSAKSI)
    tanggal = models.DateTimeField(auto_now_add=True)
    catatan = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.tipe} - {self.barang.nama_barang} ({self.jumlah})"