# Generated by Django 2.1.3 on 2019-03-14 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20190314_0508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='reserve',
            new_name='borrow',
        ),
    ]