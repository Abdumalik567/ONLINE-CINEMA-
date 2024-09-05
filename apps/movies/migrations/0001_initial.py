# Generated by Django 5.1 on 2024-08-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='movies/videos/')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='movies/pictures/')),
            ],
        ),
    ]