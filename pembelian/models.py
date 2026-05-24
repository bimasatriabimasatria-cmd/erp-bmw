from django.db import models
from master_data.models import Barang

class PurchaseOrder(models.Model):
    STATUS_PO = [
        ('DRAFT', 'Draft'),
        ('DIKIRIM', 'Dikirim ke Supplier'),
        ('DITERIMA', 'Barang Diterima'),
    ]
    nomor_po = models.CharField(max_length=50, unique=True)
    supplier = models.CharField(max_length=200)
    tanggal_po = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_PO, default='DRAFT')

    def __str__(self):
        return f"{self.nomor_po} - {self.supplier}"

class PurchaseItem(models.Model):
    po = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    barang = models.ForeignKey(Barang, on_delete=models.RESTRICT)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    harga_satuan = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.barang.nama_barang} ({self.jumlah})"