# Generated by Django 2.1.13 on 2020-03-17 05:33

import backend.media_filer.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend_media_filer', '0004_auto_20200317_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image_ptr__file', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='image_ptr',
            field=backend.media_filer.fields.CroppableFilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='backend_media_filer_filerimage_file', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
