# Generated by Django 2.2.3 on 2019-08-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190814_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messege',
            name='messege_from',
            field=models.TextField(default=None),
        ),
    ]
