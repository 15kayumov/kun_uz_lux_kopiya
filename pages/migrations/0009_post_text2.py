# Generated by Django 5.1.2 on 2024-11-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_post_delete_firstpost_delete_secondpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
