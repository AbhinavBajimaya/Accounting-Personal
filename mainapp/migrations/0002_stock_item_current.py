# Generated by Django 3.2 on 2021-06-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_item',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
