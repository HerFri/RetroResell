# Generated by Django 3.2.23 on 2024-01-25 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiries', '0003_alter_inquiry_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_message', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('inquiry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inquiries.inquiry')),
            ],
        ),
    ]
