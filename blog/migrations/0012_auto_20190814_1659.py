# Generated by Django 2.2.3 on 2019-08-14 11:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Messege',
        ),
        migrations.RenameField(
            model_name='messege',
            old_name='message',
            new_name='messege',
        ),
    ]
