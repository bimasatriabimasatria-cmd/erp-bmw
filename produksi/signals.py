from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WorkOrder
from inventaris.models import Stok, TransaksiStok

@receiver(post_save, sender=WorkOrder)
def proses_stok_otomatis(sender, instance, created, **kwargs):
    # Hanya jalan jika status SELESAI dan belum pernah diproses sebelumnya
    if instance.status == 'SELESAI' and not instance.is_processed:
        
        # 1. TAMBAH STOK BARANG JADI (Hasil Produksi)
        stok_jadi, created = Stok.objects.get_or_create(barang=instance.resep.produk_hasil)
        stok_jadi.jumlah += instance.target_produksi
        stok_jadi.save()
        
        # Catat ke log transaksi
        TransaksiStok.objects.create(
            barang=instance.resep.produk_hasil,
            jumlah=instance.target_produksi,
            tipe='MASUK',
            catatan=f"Hasil Produksi dari WO: {instance.nomor_wo}"
        )

        # 2. KURANGI STOK BAHAN BAKU (Komponen Resep)
        for komponen in instance.resep.komponenresep_set.all():
            jumlah_pakai = komponen.jumlah_dibutuhkan * instance.target_produksi
            
            stok_baku = Stok.objects.get(barang=komponen.bahan_baku)
            stok_baku.jumlah -= jumlah_pakai
            stok_baku.save()
            
            # Catat ke log transaksi
            TransaksiStok.objects.create(
                barang=komponen.bahan_baku,
                jumlah=jumlah_pakai,
                tipe='KELUAR',
                catatan=f"Pemakaian Produksi untuk WO: {instance.nomor_wo}"
            )

        # 3. Kunci WO agar tidak diproses ulang
        instance.is_processed = True
        instance.save()