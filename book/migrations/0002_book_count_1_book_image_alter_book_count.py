# Generated by Django 5.0.6 on 2024-07-11 11:52

import book.helpers
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_1',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, unique=True, upload_to=book.helpers.SaveMedia.save_book_image_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
