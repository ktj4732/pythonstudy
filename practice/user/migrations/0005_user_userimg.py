# Generated by Django 3.1.2 on 2020-10-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201026_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userimg',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='유저이미지'),
        ),
    ]
