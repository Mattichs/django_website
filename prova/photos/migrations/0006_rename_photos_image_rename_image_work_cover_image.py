# Generated by Django 4.2 on 2023-05-04 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_work_photos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='image',
            new_name='cover_image',
        ),
    ]
