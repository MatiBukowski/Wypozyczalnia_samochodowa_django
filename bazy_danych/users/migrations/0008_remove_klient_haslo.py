# Generated by Django 5.1.3 on 2024-12-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_klient_groups_klient_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klient',
            name='haslo',
        ),
    ]
