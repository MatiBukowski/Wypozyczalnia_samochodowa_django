# Generated by Django 5.1.3 on 2024-11-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_users_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprzet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_sprzetu', models.IntegerField()),
                ('marka', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=20)),
                ('silnik', models.CharField(max_length=5)),
                ('moc', models.IntegerField()),
                ('moment_obrotowy', models.IntegerField()),
                ('lokalizacja', models.CharField(max_length=50)),
                ('status_dostepnosci', models.CharField(max_length=15)),
                ('typ_sprzetu', models.CharField(max_length=30)),
                ('status_zamkniecia', models.CharField(max_length=15)),
                ('status_zablokowania', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
