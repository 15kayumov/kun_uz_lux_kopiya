# Generated by Django 5.1.4 on 2024-12-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_remove_mir_img_card_remove_mir_text_card_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obshestvo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('text', models.TextField()),
                ('title2', models.CharField(max_length=200)),
                ('text2', models.TextField()),
            ],
        ),
    ]
