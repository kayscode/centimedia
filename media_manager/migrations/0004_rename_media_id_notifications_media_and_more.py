# Generated by Django 4.2.5 on 2023-10-15 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_manager', '0003_remove_mediafile_is_approved_mediafile_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='media_id',
            new_name='media',
        ),
        migrations.RenameField(
            model_name='notificationssourcemedia',
            old_name='source_id',
            new_name='source',
        ),
    ]
