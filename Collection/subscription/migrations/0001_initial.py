# Generated by Django 2.1.15 on 2020-07-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('status', models.CharField(blank=True, max_length=64)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
