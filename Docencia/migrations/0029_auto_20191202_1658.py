# Generated by Django 2.1.3 on 2019-12-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0028_auto_20191202_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupinformation',
            name='delayPerm',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='groupinformation',
            name='duration',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='groupinformation',
            name='startTime',
            field=models.TimeField(default='18:00'),
        ),
    ]