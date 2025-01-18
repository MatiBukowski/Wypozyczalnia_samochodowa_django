# Generated by Django 5.1.3 on 2024-12-09 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0023_alter_rezerwacja_id_rezerwacji'),
        ('users', '0010_pracownik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powiadomienie',
            name='ID_pracownika',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.pracownik'),
        ),
        migrations.AlterField(
            model_name='usterka',
            name='ID_pracownika_naprawiajacego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.pracownik'),
        ),
        migrations.DeleteModel(
            name='Pracownik',
        ),
    ]
