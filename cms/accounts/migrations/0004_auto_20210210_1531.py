# Generated by Django 3.1.3 on 2021-02-10 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_song_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='on_trending',
            new_name='trending',
        ),
    ]