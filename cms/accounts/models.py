from django.db import models
# Models Starts here


class Category (models.Model):
    category_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.category_name


class Language (models.Model):
    language_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.language_name


class Artist (models.Model):
    name = models.CharField(max_length=50, default="")
    front_page = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Song (models.Model):
    name = models.CharField(max_length=50, default="")
    song = models.FileField(upload_to='songs/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default="")
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default="")
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, default="")
    trending = models.BooleanField(default=True)
    banner = models.BooleanField(default=False)

    def __str__(self):
        return self.name
