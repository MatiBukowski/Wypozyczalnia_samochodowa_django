# Generated by Django 5.1.3 on 2024-11-26 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0020_alter_powiadomienie_id_klienta_and_more'),
        ('users', '0002_alter_klient_id_klienta_alter_klient_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powiadomienie',
            name='ID_klienta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.klient'),
        ),
        migrations.AlterField(
            model_name='powiadomienie',
            name='ID_pracownika',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.pracownik'),
        ),
    ]
