# Generated by Django 3.1.7 on 2021-04-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenthi', '0002_auto_20210408_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('do', models.TextField(max_length=200)),
            ],
        ),
    ]
