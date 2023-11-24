# Generated by Django 3.2.23 on 2023-11-24 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('genre', models.CharField(blank=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Arcade', 'Arcade'), ('Beat Em Up', 'Beat Em Up'), ('Ego-Shooter', 'Ego-Shooter'), ("Jump 'n' Run", "Jump 'n' Run"), ('Racing', 'Racing'), ('RPG', 'RPG'), ('Simulation', 'Simulation'), ('Sports', 'Sports'), ('Strategy', 'Strategy'), ('Puzzle', 'Puzzle'), ('Horror', 'Horror')], max_length=100, null=True)),
                ('platform', models.CharField(blank=True, choices=[('Dreamcast', 'Dreamcast'), ('Gameboy', 'Gameboy'), ('Gameboy Color', 'Gameboy Color'), ('NES', 'NES'), ('N64', 'N64'), ('PC', 'PC'), ('PlayStation', 'PlayStation'), ('PlayStation 2', 'PlayStation 2'), ('Sega Genesis', 'Sega Genesis'), ('SNES', 'SNES'), ('XBOX', 'XBOX')], max_length=100, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(choices=[(0, '0.0 Stars'), (0.5, '0.5 Stars'), (1, '1.0 Stars'), (1.5, '1.5 Stars'), (2, '2.0 Stars'), (2.5, '2.5 Stars'), (3, '3.0 Stars'), (3.5, '3.5 Stars'), (4, '4.0 Stars'), (4.5, '4.5 Stars'), (5, '5.0 Stars')], decimal_places=1, default=0, max_digits=2)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
