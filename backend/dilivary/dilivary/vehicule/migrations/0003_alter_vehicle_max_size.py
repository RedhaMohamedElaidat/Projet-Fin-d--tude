# Generated by Django 5.0.4 on 2024-04-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicule', '0002_alter_vehicle_id_driving_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='max_size',
            field=models.CharField(choices=[('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small'), ('Very Large', 'Very Large')], max_length=20),
        ),
    ]
