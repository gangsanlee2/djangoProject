# Generated by Django 4.1.3 on 2022-11-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('s_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('address', models.TextField()),
                ('detail_address', models.TextField()),
                ('phone', models.TextField()),
                ('s_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_users.suser')),
            ],
            options={
                'db_table': 's_deliveries',
            },
        ),
    ]
