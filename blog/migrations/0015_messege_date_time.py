# Generated by Django 2.2.3 on 2019-08-16 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190814_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='messege',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
