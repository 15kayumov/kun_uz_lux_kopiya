# Generated by Django 5.1.2 on 2024-11-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_carusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
