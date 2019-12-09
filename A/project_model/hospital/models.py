from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama             = models.CharField(max_length=100)
    nomor_telepon    = models.CharField(max_length=20)
    bidang           = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
        ('Minggu', 'Minggu')
    )
    jadwal_praktek     = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.nama}, nomor telepon {self.nomor_telepon}, bidang {self.bidang}, jadwal_praktek {self.jadwal_praktek}'

class Pasien(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    alamat          = models.TextField(max_length=200)
    keluhan         = models.TextField(max_length=200)
    def __str__(self):
        return f'{self.nama}, nomor_telepon {self.nomor_telepon}, alamat{self.alamat}, keluhan : {self.keluhan}'

class Resep(models.Model):
    nama            = models.CharField(max_length=100)
    total_harga     = models.IntegerField()
    kumpulan_obat   = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nama}, total harga : {self.total_harga} Rupiah, kumpulan obat : {self.kumpulan_obat}'

class Obat(models.Model):
    nama            = models.CharField(max_length=100)
    kandungan       = models.TextField(max_length=300)
    khasiat         = models.TextField(max_length=300)
    def __str__(self):
        return f'{self.nama}, kandungan :  {self.kandungan}, khasiat : {self.khasiat}'
    