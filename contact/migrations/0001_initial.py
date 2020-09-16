# Generated by Django 3.1.1 on 2020-09-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Infos',
            },
        ),
    ]
