# Generated by Django 5.0.7 on 2024-07-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Phone', models.TextField(max_length=11)),
                ('Email', models.EmailField(max_length=50)),
                ('hour', models.CharField(choices=[(9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17)], default='9.00', max_length=5)),
            ],
        ),
    ]