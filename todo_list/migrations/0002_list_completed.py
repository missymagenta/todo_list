# Generated by Django 2.2.1 on 2019-06-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
