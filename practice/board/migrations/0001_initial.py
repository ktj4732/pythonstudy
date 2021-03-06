# Generated by Django 3.1.2 on 2020-10-22 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='글제목')),
                ('contents', models.TextField(verbose_name='글내용')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
            ],
        ),
    ]
