# Generated by Django 5.0.6 on 2024-06-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentmodel',
            name='serial_number',
            field=models.CharField(max_length=255, verbose_name='Серийный номер'),
        ),
        migrations.AddConstraint(
            model_name='equipmentmodel',
            constraint=models.UniqueConstraint(condition=models.Q(('archived', False)), fields=('serial_number', 'archived'), name='equipmentmodel_unique_serial_number'),
        ),
    ]
