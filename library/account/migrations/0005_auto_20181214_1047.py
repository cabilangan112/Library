# Generated by Django 2.1.3 on 2018-12-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
            preserve_default=False,
        ),
    ]