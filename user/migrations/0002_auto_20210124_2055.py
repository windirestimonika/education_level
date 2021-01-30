# Generated by Django 3.1.4 on 2021-01-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
                ('education_level', models.CharField(max_length=100)),
                ('majors', models.CharField(max_length=100)),
                ('entry_date', models.DateField(max_length=100)),
                ('graduate_date', models.DateField(max_length=100)),
                ('scholarship', models.BooleanField(default=False)),
                ('grade', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='employees',
        ),
    ]
