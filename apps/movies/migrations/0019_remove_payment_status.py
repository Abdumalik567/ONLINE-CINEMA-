# Generated by Django 5.1 on 2024-08-28 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]
