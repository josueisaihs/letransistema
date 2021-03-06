# Generated by Django 2.1.3 on 2019-03-15 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0002_auto_20190313_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='image',
            field=models.FileField(blank=True, default='static/image/perfil/student/perfildefault.png', null=True, upload_to='static/image/perfil/teacher/'),
        ),
        migrations.AlterField(
            model_name='teacherpersonalinformation',
            name='degree',
            field=models.CharField(choices=[('Ing.', 'Ingeniero'), ('Lic.', 'Licenciado'), ('Ms.C.', 'Master en Ciencias'), ('Dr.C.', 'Doctor en Ciencias'), ('PhD.C.', 'Postdoctor en Ciencias'), ('Ning.', 'Ninguno')], default='Lic.', max_length=20),
        ),
    ]
