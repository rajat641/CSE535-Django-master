# Generated by Django 2.2.7 on 2019-11-13 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('topic1', models.CharField(max_length=50)),
                ('topic2', models.CharField(max_length=100)),
                ('topic3', models.CharField(max_length=100)),
                ('topic4', models.CharField(max_length=100)),
                ('topic5', models.CharField(max_length=100)),
            ],
        ),
    ]
