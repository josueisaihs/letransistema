import datetime, os

from django.db import models
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User


class TeacherPersonalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=2)

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    gender = models.CharField(max_length=1, choices=(("m", "Masculino"), ("f", "Femenino")), default="m")

    numberidentification = models.CharField(max_length=11, unique=True)

    street = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)

    cellphone = models.CharField(max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=8, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    image = models.FileField(upload_to=os.path.join('static', 'image', 'perfil', 'teacher'),
                             default=os.path.join('static', 'image', 'perfil', 'teacher', 'perfildefault.png'), 
                             null=True, blank=True)

    nacionality = models.CharField(max_length=50, blank=False, null=False, default="cubana")
    pasaport = models.CharField(max_length=10, blank=True, null=True)

    degree = models.CharField(max_length=20,
                              choices=(("Ing.", "Ingeniero"), ("Lic.", "Licenciado"), ("Ms.C.", "Master en Ciencias"),
                                       ("Dr.C.", "Doctor en Ciencias"), ("PhD.C.", "Postdoctor en Ciencias"),
                                       ("Ning.", "Ninguno")),
                              default="Lic.")
    title = models.CharField(max_length=100, blank=True, null=True, default="")

    def __str__(self):
        return "%s %s" % (self.name, self.lastname)

    class Meta:
        unique_together = [('name', 'lastname', 'numberidentification')]

    class Admin(ModelAdmin):
        fields = ["user", "name", "lastname", "gender", "numberidentification", "street", "city", "state", "cellphone", "phone",
                  "email", "image", "nacionality", "pasaport"]
        ordering = ["numberidentification", "lastname", "name"]
        search_fields = fields
        list_display = fields

    def eliminarTildes(self, txt):
        w = (
            ("á", "a"), 
            ("é", "e"), 
            ("í", "i"), 
            ("ó", "o"), 
            ("ú", "u"),
            ("ñ", "n")
        )
        for x, y in w:
            txt = txt.replace(x, y)
        return txt        

    def createUser(self):
        username = self.eliminarTildes(self.name.lower()[:1] + self.lastname.lower().replace(" ", ""))

        password = self.eliminarTildes("@_" + self.numberidentification + "_" + self.name.lower()[:1] + self.lastname.lower()[:1])

        user = User.objects.create_user(
            username, 
            password=password,
            first_name=self.name,
            last_name=self.lastname
        )
        user.save()

        user = User.objects.get(
            username=username, 
            first_name=self.name, 
            last_name=self.lastname
        )
        return user
# <> fin TeacherPersonalInformation


class StudentPersonalInformation(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    gender = models.CharField(max_length=1, choices=(("m", "Masculino"), ("f", "Femenino")), default="m")

    numberidentification = models.CharField(max_length=11, unique=True)

    nacionality = models.CharField(max_length=50, blank=False, null=False, default="cubana")

    street = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)

    cellphone = models.CharField(max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=8, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    image = models.FileField(upload_to=os.path.join('static', 'image', 'perfil', 'student'),
                             default=os.path.join('static', 'image', 'perfil', 'student', 'perfildefault.png'), 
                             null=True, blank=True)

    degree = models.CharField(max_length=20,
                              choices=(("Ing.", "Ingeniero"), ("Lic.", "Licenciado"), ("Ms.C.", "Master en Ciencias"),
                                       ("Dr.C.", "Doctor en Ciencias"), ("PhD.C.", "Postdoctor en Ciencias"),
                                       ("Ning.", "Ninguno")),
                              default="Ning.")
    title = models.CharField(max_length=100, blank=True, null=True, default="")

    ocupation = models.CharField(max_length=2,
                                 choices=(("te", "Trabajador Estatal"), ("ac", "Ama/o de Casa"),
                                          ("tp", "Trabajador Privado"), ("do", "Desocupado"), ("es", "Estudiante")),
                                 default="do")

    def __str__(self):
        return "%s %s" % (self.name, self.lastname)

    class Meta:
        unique_together = [('name', 'lastname', 'numberidentification')]

    class Admin(ModelAdmin):
        fields = ["name", "lastname", "gender", "numberidentification", "street", "city", "state", "cellphone", "phone",
                  "email", "image", "nacionality", "ocupation",
        ]
        ordering = ["numberidentification", "lastname", "name"]
        search_fields = fields
        list_display = fields
# <> fin StudentPersonalInformation


class CourseInformation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.FileField(upload_to=os.path.join('static', 'image', 'perfil', 'course'),
                             default=os.path.join('static', 'image', 'perfil', 'course', 'perfildefault.png'), 
                             null=True, blank=True)
    capacity = models.PositiveSmallIntegerField(default=12)
    openregistre = models.DateField(blank=True)
    deadline = models.DateField(blank=True)
    description = models.CharField(max_length=1500, blank=True)

    yearMin = models.PositiveSmallIntegerField(default=18)
    yearMax = models.PositiveSmallIntegerField(default=40)

    groups = []

    def __str__(self):
        return "%s" % (self.name)

    class Admin(ModelAdmin):
        fields = ["name", "image", "capacity", "openregistre", "deadline", "description", "yearMin", "yearMax"]
        ordering = ["name", "capacity", "openregistre"]
        search_fields = ["name", "openregistre"]
        list_display = ["name", "image", "capacity", "openregistre", "deadline"]
# <> fin CourseInformation


class ClassRoom(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return "%s" % self.name

    class Admin(ModelAdmin):
        fields = ["name"]
        ordering = fields
        list_display = fields
# <> fin ClassRoom


class GroupInformation(models.Model):
    name = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(CourseInformation, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherPersonalInformation, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, default=1)
    edition = models.CharField(max_length=9, default="%s-%s" % (datetime.datetime.today().year,
                                                                datetime.datetime.today().year + 1))
    current = models.BooleanField(default=False)
    startTime = models.TimeField(default="18:00")
    duration = models.PositiveIntegerField(default=1) # Horas
    delayPerm = models.PositiveIntegerField(default=5) # Minutos dnd se permite la llegada despues de la hora de inicio

    class Meta:
        unique_together = [('name', 'course', 'teacher', 'edition', 'classroom')]

    def __str__(self):
        return "%s (%s) - %s - %s %s" % (self.name,  self.edition, self.course.name, self.teacher.name, self.teacher.lastname)

    class Admin(ModelAdmin):
        fields = ["name", "course", "teacher", "edition", "current", "classroom", "startTime", "duration", "delayPerm"]
        ordering = ["name"]
        search_fields = ["name"]
        list_display = fields
# <> fin GroupInformation


class Candidate(models.Model):
    course = models.ForeignKey(CourseInformation, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentPersonalInformation, on_delete=models.CASCADE)
    interview = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.course, self.student, self.interview)

    class Admin(ModelAdmin):
        fields = ["course", "student", "interview", "recommended", "selected"]
        ordering = ["course"]
        list_display = fields
# <> fin Candidate


class GroupList(models.Model):
    group = models.ForeignKey(GroupInformation, on_delete=models.CASCADE)
    student = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    inasistencias = 0
    tardanzas = 0
    asistenciaHoy = False

    def __str__(self):
        return "%s %s" % (self.group.name, self.student)

    class Meta:
        unique_together = [('group', 'student')]

    class Admin(ModelAdmin):
        fields = ["group", "student"]
        ordering = ["group"]
        list_display = fields
# <> fin GroupList


class Assistence(models.Model):
    assis_dateTime = models.DateTimeField(blank=True)
    assis_grouplist = models.ForeignKey(GroupList, on_delete=models.CASCADE)
    assis_status = models.CharField(
        max_length=1,
        choices=(
            ("a", "Asistencia"), 
            ("i", "Inasistencia"),
            ("t", "Tardanza")
        ),
        default="a"
    )
    assis_mode = models.CharField(max_length=1, choices=(
        (("m", "Manual"), ("a", "Auto"))
    ), default="m")

    def __str__(self):
        return "%s %s %s" % (self.assis_dateTime, self.assis_grouplist.student, self.assis_status)

    class Admin(ModelAdmin):
        fields = ["assis_dateTime", "assis_grouplist", "assis_status", "assis_mode"]
        ordering = ["assis_dateTime"]
        list_display = fields
# <> fin Assistence

class Raspberrys(models.Model):
    name = models.CharField(max_length=50, null=False)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.classroom)
    
    class Admin(ModelAdmin):
        fields = ["name", "classroom"]
        ordering = ["name"]
        list_display = ["name", "classroom"]
# <> fin Raspberrys
