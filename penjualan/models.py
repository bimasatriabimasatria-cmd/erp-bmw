from django.db import models
from master_data.models import Barang

class SalesOrder(models.Model):
    STATUS_SALES = [
        ('DRAFT', 'Draft'),
        ('SELESAI', 'Selesai/Dikirim'),
    ]
    nomor_so = models.CharField(max_length=50, unique=True)
    pelanggan = models.CharField(max_length=200)
    tanggal_so = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_SALES, default='DRAFT')

    def __str__(self):
        return f"{self.nomor_so} - {self.pelanggan}"

class SalesItem(models.Model):
    so = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    barang = models.ForeignKey(Barang, on_delete=models.RESTRICT)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    harga_jual = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.barang.nama_barang} ({self.jumlah})"