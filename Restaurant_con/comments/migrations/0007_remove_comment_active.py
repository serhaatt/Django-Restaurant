# Generated by Django 5.0.7 on 2024-07-18 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]
