# Generated by Django 3.2.23 on 2023-12-15 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_user',
            new_name='user',
        ),
    ]