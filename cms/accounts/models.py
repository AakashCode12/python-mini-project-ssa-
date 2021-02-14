from django.db import models
# Models Starts here


class Album (models.Model):
    album_name = models.CharField(max_length=50, default="")
    album_image = models.ImageField(
        upload_to="album-images/", default="", blank=True)

    def __str__(self):
        return self.album_name


class Language (models.Model):
    language_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.language_name


class Artist (models.Model):

    # There must be 4 Artists at the Front Page I mean front page true
    name = models.CharField(max_length=50, default="")
    front_page = models.BooleanField(default=False)
    artist_image = models.ImageField(upload_to="artist-images/", default="")

    def __str__(self):
        return self.name


class Song (models.Model):
    name = models.CharField(max_length=50, default="")
    song = models.FileField(upload_to='songs/')
    Album = models.ForeignKey(
        Album, on_delete=models.CASCADE, default="")
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default="")
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, default="")
    song_image = models.ImageField(upload_to="song-images/", default="")
    trending = models.BooleanField(default=True)
    # banner = models.BooleanField(default=False)

    def __str__(self):
        return self.name
