# Generated by Django 3.1.4 on 2021-01-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('schoolname', models.CharField(max_length=100)),
                ('educationlevel', models.CharField(max_length=100)),
                ('majors', models.CharField(max_length=100)),
            ],
        ),
    ]
