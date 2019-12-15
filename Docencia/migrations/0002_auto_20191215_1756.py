# Generated by Django 2.1.3 on 2019-12-15 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Docencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assis_dateTime', models.DateTimeField(blank=True)),
                ('assis_status', models.CharField(choices=[('a', 'Asistencia'), ('i', 'Inasistencia'), ('t', 'Tardanza')], default='a', max_length=1)),
                ('assis_mode', models.CharField(choices=[('m', 'Manual'), ('a', 'Auto')], default='m', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview', models.BooleanField(default=False)),
                ('recommended', models.BooleanField(default=False)),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.FileField(blank=True, default='static/image/perfil/course/perfildefault.png', null=True, upload_to='static/image/perfil/course')),
                ('capacity', models.PositiveSmallIntegerField(default=12)),
                ('openregistre', models.DateField(blank=True)),
                ('deadline', models.DateField(blank=True)),
                ('description', models.CharField(blank=True, max_length=1500)),
                ('yearMin', models.PositiveSmallIntegerField(default=18)),
                ('yearMax', models.PositiveSmallIntegerField(default=40)),
            ],
        ),
        migrations.CreateModel(
            name='GroupInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('edition', models.CharField(default='2019-2020', max_length=9)),
                ('current', models.BooleanField(default=False)),
                ('startTime', models.TimeField(default='18:00')),
                ('duration', models.PositiveIntegerField(default=1)),
                ('delayPerm', models.PositiveIntegerField(default=5)),
                ('classroom', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Docencia.ClassRoom')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.CourseInformation')),
            ],
        ),
        migrations.CreateModel(
            name='GroupList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.GroupInformation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Raspberrys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], default='m', max_length=1)),
                ('numberidentification', models.CharField(max_length=11, unique=True)),
                ('nacionality', models.CharField(default='cubana', max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cellphone', models.CharField(blank=True, max_length=8, null=True)),
                ('phone', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.FileField(blank=True, default='static/image/perfil/student/perfildefault.png', null=True, upload_to='static/image/perfil/student')),
                ('degree', models.CharField(choices=[('Ing.', 'Ingeniero'), ('Lic.', 'Licenciado'), ('Ms.C.', 'Master en Ciencias'), ('Dr.C.', 'Doctor en Ciencias'), ('PhD.C.', 'Postdoctor en Ciencias'), ('Ning.', 'Ninguno')], default='Ning.', max_length=20)),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ocupation', models.CharField(choices=[('te', 'Trabajador Estatal'), ('ac', 'Ama/o de Casa'), ('tp', 'Trabajador Privado'), ('do', 'Desocupado'), ('es', 'Estudiante')], default='do', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='teacherpersonalinformation',
            name='degree',
            field=models.CharField(choices=[('Ing.', 'Ingeniero'), ('Lic.', 'Licenciado'), ('Ms.C.', 'Master en Ciencias'), ('Dr.C.', 'Doctor en Ciencias'), ('PhD.C.', 'Postdoctor en Ciencias'), ('Ning.', 'Ninguno')], default='Lic.', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacherpersonalinformation',
            name='image',
            field=models.FileField(blank=True, default='static/image/perfil/teacher/perfildefault.png', null=True, upload_to='static/image/perfil/teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='studentpersonalinformation',
            unique_together={('name', 'lastname', 'numberidentification')},
        ),
        migrations.AddField(
            model_name='groupinformation',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.TeacherPersonalInformation'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.CourseInformation'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.StudentPersonalInformation'),
        ),
        migrations.AddField(
            model_name='assistence',
            name='assis_grouplist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Docencia.GroupList'),
        ),
        migrations.AlterUniqueTogether(
            name='grouplist',
            unique_together={('group', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='groupinformation',
            unique_together={('name', 'course', 'teacher', 'edition', 'classroom')},
        ),
    ]