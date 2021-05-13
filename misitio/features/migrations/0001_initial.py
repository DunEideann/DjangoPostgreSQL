# Generated by Django 3.1.7 on 2021-04-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('link', models.CharField(default='No link available', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('do', models.TextField(max_length=200)),
                ('privacy', models.BooleanField(default=True)),
            ],
        ),
    ]
