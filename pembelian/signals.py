from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from inventaris.models import Stok, TransaksiStok

@receiver(post_save, sender=PurchaseOrder)
def update_stok_pembelian(sender, instance, created, **kwargs):
    if instance.status == 'DITERIMA':
        for item in instance.items.all():
            # Tambah atau Update Stok
            stok, _ = Stok.objects.get_or_create(barang=item.barang)
            stok.jumlah += item.jumlah
            stok.save()
            
            # Catat Transaksi
            TransaksiStok.objects.create(
                barang=item.barang,
                jumlah=item.jumlah,
                tipe='MASUK',
                catatan=f"Pembelian PO: {instance.nomor_po}"
            )