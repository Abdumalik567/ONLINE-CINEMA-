# Generated by Django 5.1 on 2024-08-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0002_rename_capacity_hall_rows_hall_seats_in_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='rows',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
