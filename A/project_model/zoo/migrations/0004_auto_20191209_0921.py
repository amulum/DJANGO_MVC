# Generated by Django 3.0 on 2019-12-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_auto_20191209_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjaga',
            name='jadwal_jaga',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200),
        ),
    ]