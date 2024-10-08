# Generated by Django 5.0.6 on 2024-07-14 10:57

import book.helpers
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_purchasedbook_wishlistbook_delete_test'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishlistBook',
            new_name='Wishlist',
        ),
        migrations.RenameField(
            model_name='purchasedbook',
            old_name='purchase_date',
            new_name='purchased_at',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='added_date',
            new_name='added_at',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=book.helpers.SaveMedia.save_book_image_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
