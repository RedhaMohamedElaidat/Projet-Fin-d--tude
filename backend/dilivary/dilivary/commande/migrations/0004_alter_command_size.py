# Generated by Django 5.0.4 on 2024-05-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0003_command_desqreption_command_idclient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='size',
            field=models.CharField(choices=[('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small'), ('Very Large', 'Very Large')], max_length=20),
        ),
    ]
