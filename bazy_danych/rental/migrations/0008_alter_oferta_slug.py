# Generated by Django 5.1.3 on 2024-11-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_oferta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
