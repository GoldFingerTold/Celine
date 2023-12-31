# Generated by Django 4.2.4 on 2023-08-16 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='prensa')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Prensa',
                'verbose_name_plural': 'Prensas',
            },
        ),
        migrations.CreateModel(
            name='imagePrensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prensa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prensa.prensa')),
            ],
        ),
    ]
