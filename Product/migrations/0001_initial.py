# Generated by Django 5.0.7 on 2024-07-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=300)),
                ('is_active', models.BooleanField(default=False)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]
