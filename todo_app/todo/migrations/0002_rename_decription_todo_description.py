# Generated by Django 3.2.20 on 2023-07-13 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='decription',
            new_name='description',
        ),
    ]
