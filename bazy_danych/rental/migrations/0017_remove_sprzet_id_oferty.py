# Generated by Django 5.1.3 on 2024-11-22 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0016_sprzet_id_oferty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprzet',
            name='ID_oferty',
        ),
    ]
