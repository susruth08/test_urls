# Generated by Django 2.2.5 on 2020-01-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lcmurl',
            name='url_string',
            field=models.TextField(unique=True),
        ),
    ]
