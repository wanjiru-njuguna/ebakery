# Generated by Django 4.2.9 on 2024-04-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0011_cartitems_is_toppick'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='is_toppick',
            field=models.BooleanField(default=True),
        ),
    ]
