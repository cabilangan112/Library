# Generated by Django 2.1.3 on 2019-02-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_user_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Year',
            field=models.CharField(blank=True, choices=[('1st', 'Firs Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4rt', 'Fourth Year'), ('Personal', 'Personal')], default=True, max_length=6),
        ),
    ]
