# Generated by Django 4.1.4 on 2022-12-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('birth', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=20)),
                ('user_interests', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'z_users',
                'db_table': 'z_users',
            },
        ),
    ]
