# Generated by Django 3.1.3 on 2021-02-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210210_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='front_page',
            field=models.BooleanField(default=False),
        ),
    ]
