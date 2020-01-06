# Generated by Django 2.1.5 on 2019-11-21 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='user',
        ),
        migrations.AddField(
            model_name='preferences',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authen.Appuser'),
        ),
    ]
