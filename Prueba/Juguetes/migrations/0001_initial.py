# Generated by Django 4.1.3 on 2022-11-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juguetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20)),
                ('producto', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=10)),
                ('precio', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=5)),
                ('marca', models.CharField(max_length=20)),
                ('tienda', models.CharField(max_length=20))
            ],
        ),
    ]
