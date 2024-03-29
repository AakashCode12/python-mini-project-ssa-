# Generated by Django 3.1.3 on 2021-02-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_artist_front_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(default='', upload_to='artist-images/'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='', upload_to='category-images/'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_image',
            field=models.ImageField(default='', upload_to='song-images/'),
        ),
    ]
