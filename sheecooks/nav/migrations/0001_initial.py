# Generated by Django 4.2.9 on 2024-02-20 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('date', models.DateField()),
                ('product_name', models.CharField(max_length=100)),
                ('product_serial_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('opening_balance', models.IntegerField()),
                ('closing_balance', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('product_buying_price', models.FloatField(max_length=100)),
                ('product_selling_price', models.FloatField(max_length=100)),
                ('sales_tax', models.FloatField(max_length=20)),
                ('sale_discount', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(max_length=100)),
                ('user_last_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(default='Zanesville', max_length=64)),
                ('state', models.CharField(default='OH', max_length=128)),
                ('zip_code', models.CharField(default='43701', max_length=5)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.users')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='user_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.users_addresses'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField()),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.users_addresses')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.users')),
                ('product_ordered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nav.product')),
            ],
        ),
    ]
