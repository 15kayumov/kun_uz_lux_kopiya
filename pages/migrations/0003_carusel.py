# Generated by Django 5.1.2 on 2024-11-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post_text_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, upload_to='')),
                ('img2', models.ImageField(blank=True, upload_to='')),
                ('img3', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
