# Generated by Django 2.1.3 on 2019-11-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0021_candidate_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupinformation',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]