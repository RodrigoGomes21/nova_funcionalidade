# Generated by Django 3.2.18 on 2024-10-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0004_alter_time_modalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='modalidade',
            field=models.CharField(choices=[('basquete', 'Basquete'), ('futsal', 'Futsal'), ('handebol', 'Handebol'), ('volei', 'Volei')], max_length=50),
        ),
    ]
