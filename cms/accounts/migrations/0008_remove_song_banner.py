# Generated by Django 3.1.3 on 2021-02-12 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210212_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='banner',
        ),
    ]
