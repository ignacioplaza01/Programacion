# Generated by Django 4.1.3 on 2022-11-30 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
        ('Juguetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguetes',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.tienda'),
        ),
    ]