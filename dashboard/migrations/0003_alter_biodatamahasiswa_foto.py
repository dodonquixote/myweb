# Generated by Django 5.0.6 on 2024-08-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_biodatamahasiswa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodatamahasiswa',
            name='foto',
            field=models.ImageField(default='default.jpg', upload_to='templates/img'),
        ),
    ]
