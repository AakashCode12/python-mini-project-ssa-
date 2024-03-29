# Generated by Django 3.1.3 on 2021-02-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('song', models.FileField(upload_to='songs/')),
                ('on_trending', models.BooleanField(default=True)),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.artist')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
                ('language', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.language')),
            ],
        ),
    ]
