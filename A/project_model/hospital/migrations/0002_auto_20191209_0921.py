# Generated by Django 3.0 on 2019-12-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resep',
            name='total_harga',
            field=models.IntegerField(),
        ),
    ]
