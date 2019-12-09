from django.db import models

# Create your models here.
class Hewan(models.Model):
    nama    = models.CharField(max_length=100)
    species = models.CharField(max_length=20)
    berat   = models.DecimalField(max_digits=10,decimal_places=2)
    umur    = models.IntegerField()
    
    def __str__(self):
        return f'{self.nama}, species {self.species}, berat {self.berat}kg, umur {self.umur}Tahun'

class Kandang(models.Model):
    nama = models.CharField(max_length=100)
    isi_kandang = models.CharField(max_length=100)
    luas_kandang = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nama}, isi kandang {self.isi_kandang}, luas {self.luas_kandang} m2'

class Penjaga(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)

    CATEGORY_CHOICES = (
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu', 'Sabtu'),
        ('Minggu', 'Minggu')
    )
    jadwal_jaga = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.nama}, nomor telepon {self.nomor_telepon}, jadwal_jaga {self.jadwal_jaga}'

class Pengunjung(models.Model):
    nama            = models.CharField(max_length=100)
    nomor_telepon   = models.CharField(max_length=20)
    hari_berkunjung = models.DateTimeField('hari berkunjung')
    def __str__(self):
        return f'{self.nama}, nomor telepon {self.nomor_telepon}, hari berkunjung {self.hari_berkunjung}'