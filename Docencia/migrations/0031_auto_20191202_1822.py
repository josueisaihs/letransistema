# Generated by Django 2.1.3 on 2019-12-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0030_assistence_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistence',
            name='status',
            field=models.CharField(choices=[('a', 'Asistencia'), ('i', 'Inasistencia'), ('t', 'Tardanza')], default='a', max_length=1),
        ),
    ]