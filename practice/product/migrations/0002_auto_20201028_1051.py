# Generated by Django 3.1.2 on 2020-10-28 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='productimg',
        ),
    ]
