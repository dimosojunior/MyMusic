# Generated by Django 4.1.3 on 2022-12-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicApp', '0002_musicvideos_artistimage_musicvideos_isfeatured_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicvideos',
            name='IsFeatured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='musicvideos',
            name='IsTrending',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='musicvideos',
            name='NewRelease',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
