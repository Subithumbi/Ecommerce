# Generated by Django 3.2.23 on 2024-01-04 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20240101_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
