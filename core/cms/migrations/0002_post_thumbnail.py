# Generated by Django 2.2 on 2020-08-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='', verbose_name='تصویر شاخص'),
            preserve_default=False,
        ),
    ]
