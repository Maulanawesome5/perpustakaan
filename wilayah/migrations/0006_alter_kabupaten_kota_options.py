# Generated by Django 4.2.11 on 2024-04-08 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wilayah', '0005_kabupaten_kota_predikat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kabupaten_kota',
            options={'ordering': ['provinsi_id', 'id']},
        ),
    ]
