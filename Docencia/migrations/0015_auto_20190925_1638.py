# Generated by Django 2.1.3 on 2019-09-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0014_auto_20190925_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='numberidentification',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
