# Generated by Django 4.2 on 2023-05-02 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_category_name_alter_photo_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='des',
            new_name='description',
        ),
    ]
