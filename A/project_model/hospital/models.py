from django.db import models

# Create your models here.
class Dokter(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    bidang          = models.CharField(max_length=100)
    jadwal_praktek  = models.CharField(max_length=100)

class Pasien(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    alamat          = models.TextField(max_length=200)
    keluhan         = models.TextField(max_length=200)

class Resep(models.Model):
    nama            = models.CharField(max_length=100)
    total_harga     = models.IntegerField()
    kumpulan_obat   = models.CharField(max_length=100)
    

class Obat(models.Model):
    nama            = models.CharField(max_length=100)
    kandungan       = models.TextField(max_length=300)
    khasiat         = models.TextField(max_length=300)
    