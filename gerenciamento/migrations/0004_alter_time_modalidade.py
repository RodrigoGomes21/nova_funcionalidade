# Generated by Django 3.2.18 on 2024-10-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='modalidade',
            field=models.CharField(choices=[('futsal', 'Futsal'), ('basquete', 'Basquete'), ('volei', 'Vôlei'), ('handebol', 'Handebol')], max_length=50),
        ),
    ]
