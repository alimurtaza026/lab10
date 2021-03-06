# Generated by Django 3.1.4 on 2020-12-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippindDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_first_name', models.CharField(max_length=50)),
                ('receiver_last_name', models.CharField(max_length=50)),
                ('receiver_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
