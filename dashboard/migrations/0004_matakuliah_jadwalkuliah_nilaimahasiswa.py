# Generated by Django 5.0.6 on 2024-08-14 12:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_biodatamahasiswa_foto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matkul', models.CharField(max_length=50)),
                ('dosen', models.CharField(max_length=50)),
                ('sks', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='JadwalKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(choices=[('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'), ('kamis', 'Kamis'), ('jumat', 'Jumat'), ('sabtu', 'Sabtu'), ('minggu', 'Minggu')], max_length=10)),
                ('jam', models.CharField(max_length=10)),
                ('matkul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.matakuliah')),
            ],
        ),
        migrations.CreateModel(
            name='NilaiMahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai_huruf', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('matkul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.matakuliah')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]