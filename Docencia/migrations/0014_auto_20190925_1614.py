# Generated by Django 2.1.3 on 2019-09-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0013_auto_20190920_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='numberidentification',
            field=models.CharField(max_length=11),
        ),
    ]
