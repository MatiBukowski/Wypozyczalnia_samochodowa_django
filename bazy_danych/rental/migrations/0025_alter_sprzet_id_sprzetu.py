# Generated by Django 5.1.3 on 2024-12-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0024_alter_powiadomienie_id_pracownika_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprzet',
            name='ID_sprzetu',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
