# Generated by Django 2.1.3 on 2019-03-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20190301_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=50, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=2000),
        ),
    ]
