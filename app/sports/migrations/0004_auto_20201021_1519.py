# Generated by Django 3.1.2 on 2020-10-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20201020_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]