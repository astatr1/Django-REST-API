# Generated by Django 4.2.9 on 2024-02-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picasso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d'),
        ),
    ]
