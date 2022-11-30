# Generated by Django 4.1.3 on 2022-11-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('deliveries', '0001_initial'),
        ('s_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveries.delivery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('s_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_users.suser')),
            ],
            options={
                'db_table': 's_orders',
            },
        ),
    ]
