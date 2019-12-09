from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama    = models.CharField(max_length=100)
    species = models.CharField(max_length=20)
    berat   = models.DecimalField(max_digits=10,decimal_places=2)
    umur    = models.IntegerField()

class Kandang(models.Model):
    nama = models.CharField(max_length=100)
    isi_kandang = models.CharField(max_length=100)
    luas_kandang = models.DecimalField(max_digits=10, decimal_places=2)


class Penjaga(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    jadwal_jaga = models.CharField(max_length=20)


class Pengunjung(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    hari_berkunjung = models.DateTimeField(auto_now=True)
