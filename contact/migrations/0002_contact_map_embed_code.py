# Generated by Django 4.2.7 on 2023-11-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='map_embed_code',
            field=models.TextField(default='MAP'),
        ),
    ]
