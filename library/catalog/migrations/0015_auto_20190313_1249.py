# Generated by Django 2.1.3 on 2019-03-13 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20190313_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserve',
            old_name='due_date',
            new_name='checkout',
        ),
    ]
