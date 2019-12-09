from django.db import models

# Create your models here.
class Direksi(models.Model):
    nama_lengkap            = models.CharField(max_length=100)
    no_telepon              = models.CharField(max_length=20)
    jabatan                 = models.CharField(max_length=20)
    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap            = models.CharField(max_length=100)
    no_telepon              = models.CharField(max_length=20)
    nomor_absen             = models.IntegerField(default=0)
    nilai_rata              = models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran          = models.CharField(max_length=100)
    jadwal_dimulai          = models.DateTimeField('jadwal dimulai')    
    jadwal_berakhir         = models.DateTimeField('jadwal berakhir')
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap            = models.CharField(max_length=100)
    no_telepon              = models.CharField(max_length=20)
    mata_pelajaran          = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_lengkap

class Challange(models.Model):
    nama_challange          = models.CharField(max_length=200)
    banyak_soal             = models.IntegerField()
    bobot_nilai             = models.CharField(max_length=100)
    mata_pelajaran          = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challange

class LiveCode(models.Model):
    nama_live_code          = models.CharField(max_length=200)
    banyak_soal             = models.IntegerField()
    bobot_nilai             = models.CharField(max_length=100)
    tanggal_pelaksanaaan    = models.DateTimeField('tanggal pelaksanaaan')
    mata_pelajaran          = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_live_code