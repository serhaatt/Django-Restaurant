# Generated by Django 5.0.7 on 2024-07-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]