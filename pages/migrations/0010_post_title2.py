# Generated by Django 5.1.2 on 2024-11-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_post_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title2',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
