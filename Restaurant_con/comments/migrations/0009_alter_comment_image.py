# Generated by Django 5.0.7 on 2024-07-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default='comments/default.jpeg', null=True, upload_to='comments/%Y/%m/%d/', verbose_name='Müşteri Resmi'),
        ),
    ]
