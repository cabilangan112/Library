# Generated by Django 2.1.3 on 2018-12-22 03:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0006_auto_20181219_0544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserved',
            new_name='Reserve',
        ),
    ]
