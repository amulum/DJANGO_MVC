# Generated by Django 3.0 on 2019-12-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=20)),
                ('berat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('umur', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('isi_kandang', models.CharField(max_length=100)),
                ('luas_kandang', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_telepon', models.IntegerField(max_length=20)),
                ('hari_berkunjung', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_telepon', models.IntegerField(max_length=20)),
                ('jadwal_jaga', models.CharField(max_length=6)),
            ],
        ),
    ]
