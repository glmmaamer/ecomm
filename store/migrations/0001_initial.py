# Generated by Django 4.2.13 on 2024-07-06 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(upload_to='upload/product')),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('city', models.CharField(max_length=150)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
