import datetime

from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, UnorderedObjectListWarning
from django.core import serializers
from django.db.models import Q
from django.views.decorators.http import require_POST

from .forms import *

from .carnetgenerador import QR

def indexEnrollment(request):
    step_2_active = "w3-text-gray w3-bottombar w3-border-gray"
    step_3_active = "w3-text-gray w3-bottombar w3-border-gray"

    error = False
    if request.method == "POST":
        studentCandidateForm = StudentCandidateForm(request.POST)
        if studentCandidateForm.is_valid():
            ci = studentCandidateForm.cleaned_data["studentCI"]

            try:
                pk = StudentPersonalInformation.objects.get(numberidentification="%s" % ci).pk
                return HttpResponseRedirect('/docencia/selectcourse/%s' % pk)
            except:
                error = True
    else:
        studentCandidateForm = StudentCandidateForm()

    return render(request, "docencia/matriculaIndex.html",  locals())
# <> indexStudent


def teacherPersonalInformation(request):
    if request.method == 'POST':
        teacherPersonalInformationForm = TeacherPersonalInformationForm(request.POST, request.FILES)
        if teacherPersonalInformationForm.is_valid():
            teacherPersonalInformationForm.save()

            return HttpResponseRedirect('/docencia/listteacher/')
    else:
        teacherPersonalInformationForm = TeacherPersonalInformationForm()

    return render(request, "docencia/newteacher.html", locals())
# <> teacherPersonalInformation


def teacherList(request):
    if request.method == "POST":
        search_text = request.POST.get('search')

        response_data = {}

        data = serializers.serialize("json", TeacherPersonalInformation.objects.
                                     filter(Q(lastname__icontains=search_text) | Q(name__icontains=search_text)).
                                     order_by('lastname')[:25])

        response_data["data"] = data

        return JsonResponse(response_data)
    else:
        teachers_total = TeacherPersonalInformation.objects.all().order_by('lastname')
        try:
            paginador = Paginator(teachers_total, 5)
            page = request.GET.get('page')

            teachers = paginador.get_page(page)
        except UnorderedObjectListWarning:
            paginador = []
            page = []

        return render(request, "docencia/listteacher.html", locals())
# <> fin teacherList


def teacherDelete(request, pk):
    teacher = TeacherPersonalInformation.objects.get(pk=pk)
    teacher.delete()

    return HttpResponseRedirect('/docencia/listteacher/')
# <> fin teacherDelete


def teacherEdit(request, pk):
    teacher = TeacherPersonalInformation.objects.get(pk=pk)
    if request.method == 'POST':
        teacherPersonalInformationForm = TeacherPersonalInformationForm(request.POST, request.FILES, instance=teacher)
        if teacherPersonalInformationForm.is_valid():
            teacherPersonalInformationForm.save()

            return HttpResponseRedirect('/docencia/listteacher/')
    else:
        teacherPersonalInformationForm = TeacherPersonalInformationForm(instance=teacher)

    return render(request, "docencia/newteacher.html", locals())
# <> fin teacherEdit


def teacherDetail(request, pk):
    teacher = TeacherPersonalInformation.objects.get(pk=pk)

    return render(request, "docencia/detailteacher.html", locals())
# <> fin teacherDetail


def studentPersonalInformation(request):
    step_2_active = "w3-text-teal w3-bottombar w3-border-teal"
    step_3_active = "w3-text-gray w3-bottombar w3-border-gray"

    if request.method == 'POST':
        studentPersonalInformationForm = StudentPersonalInformationForm(request.POST, request.FILES)
        if studentPersonalInformationForm.is_valid():
            nombre = studentPersonalInformationForm.cleaned_data["name"]
            apellido = studentPersonalInformationForm.cleaned_data["lastname"]
            ci = studentPersonalInformationForm.cleaned_data["numberidentification"]

            studentPersonalInformationForm.save()

            student = StudentPersonalInformation.objects.get(name=nombre, lastname=apellido, numberidentification=ci)
            pk = student.pk

            # Generar Codigo QR por estudiante
            qrcode = QR(ci)
            student.qrcode = qrcode.generar()
            student.save()

            return HttpResponseRedirect('/docencia/selectcourse/%s' % pk)
    else:
        studentPersonalInformationForm = StudentPersonalInformationForm()

    return render(request, "docencia/newstudent.html", locals())
# <> studentPersonalInformation


def studentList(request):
    """listado general de los estudiantes; permite hacer busquedas, modificar y eliminar estudiantes"""

    if request.method == "POST":
        search_text = request.POST.get('search')

        response_data = {}

        data = serializers.serialize("json", StudentPersonalInformation.objects.
                                     filter(Q(lastname__icontains=search_text) | Q(name__icontains=search_text)).
                                     order_by('lastname')[:25])

        response_data["data"] = data

        return JsonResponse(response_data)
    else:
        students_total = StudentPersonalInformation.objects.all().order_by('lastname')
        try:
            paginador = Paginator(students_total, 100)
            page = request.GET.get('page')

            students = paginador.get_page(page)
        except UnorderedObjectListWarning:
            paginador = []
            page = []

        return render(request, "docencia/liststudent.html", locals())
# <> fin studentList


@require_POST
def studentsCarnetAjax(request):
    students = request.POST.get("list")
    student_list = []
    for student in students:
        _student_ = StudentPersonalInformation.objects.get(pk=student)
        student_list.append({
                                 "nombre": "%s %s" % (_student_.name, _student_.lastname),
                                 "ci": _student_.numberidentification,
                                 "qr": _student_.qrcode,
                                 "perfil": _student_.image
                             })

    response_data = {"data": student_list}

    return JsonResponse(response_data)
# <> fin studentsCarnet


def studentCarnet(request, pk):
    student = StudentPersonalInformation.objects.get(pk=pk)
    return render(request, "docencia/carnet.html", locals())
# <> fin studentCarnet


def studentDelete(request, pk):
    student = StudentPersonalInformation.objects.get(pk=pk)
    student.delete()

    return HttpResponseRedirect('/docencia/liststudent/')
# <> fin studentDelete


def studentEdit(request, pk):
    if request.method == 'POST':
        studentPersonalInformationForm = StudentPersonalInformationForm(request.POST,
                                                                        request.FILES,
                                                                        instance=StudentPersonalInformation.objects.get(pk=pk))
        if studentPersonalInformationForm.is_valid():
            nombre = studentPersonalInformationForm.cleaned_data["name"]
            apellido = studentPersonalInformationForm.cleaned_data["lastname"]
            ci = studentPersonalInformationForm.cleaned_data["numberidentification"]

            studentPersonalInformationForm.save()

            # Generar Codigo QR por estudiante
            student = StudentPersonalInformation.objects.get(name=nombre,
                                                             lastname=apellido,
                                                             numberidentification=ci)
            qrcode = QR(ci)
            student.qrcode = qrcode.generar()
            student.save()

            return HttpResponseRedirect('/docencia/liststudent/')
    else:
        studentPersonalInformationForm = StudentPersonalInformationForm(instance=StudentPersonalInformation.objects.get(pk=pk))

    return render(request, "docencia/newstudent.html", locals())
# <> fin studentEdit


def courseInformation(request):
    if request.method == 'POST':
        courseInformationForm = CourseInformationForm(request.POST)

        if courseInformationForm.is_valid():
            courseInformationForm.save()

            return HttpResponseRedirect('/docencia/listcourses/')
    else:
        courseInformationForm = CourseInformationForm()

    return render(request, "docencia/newcourse.html", locals())
# <> fin courseInformation


def courseDelete(request, pk):
    course = CourseInformation.objects.get(pk=pk)
    course.delete()

    return HttpResponseRedirect('/docencia/listcourses/')
# <> fin courseDelete


def courseEdit(request, pk):
    if request.method == "POST":
        courseInformationForm = CourseInformationForm(request.POST)

        if courseInformationForm.is_valid():
            courseInformationForm.save()

            return HttpResponseRedirect('/docencia/listcourses')
    else:
        courseInformationForm = CourseInformationForm(
            instance=CourseInformation.objects.get(pk=pk))

    return render(request, "docencia/newcourse.html", locals())
# <> fin courseDelete


def groupInformation(request):
    if request.method == 'POST':
        groupInformationForm = GroupInformationForm(request.POST)
        if groupInformationForm.is_valid():
            courseId = groupInformationForm.cleaned_data['course']
            groupInformationForm.save()

            return HttpResponseRedirect('/docencia/listgroupinformation/%s' % courseId)
        else:
            teacherList = TeacherPersonalInformation.objects.all().order_by("lastname")
            courseList = CourseInformation.objects.all().order_by("name")
    else:
        groupInformationForm = GroupInformationForm()
        teacherList = TeacherPersonalInformation.objects.all().order_by("lastname")
        courseList = CourseInformation.objects.all().order_by("name")

    return render(request, "docencia/newgroup.html", locals())
# <> fin groupInformation


def selectCourse(request, pk):
    step_2_active = "w3-text-teal w3-bottombar w3-border-teal"
    step_3_active = "w3-text-teal w3-bottombar w3-border-teal"

    student = StudentPersonalInformation.objects.get(pk=pk)
    courses = CourseInformation.objects.all()

    if request.method == 'POST':
        candidateForm = CandidateSelectCourseForm(request.POST)
        if candidateForm.is_valid():
            candidateForm.save()

            return render(request, "docencia/successtudent.html", locals())
    else:
        candidateForm = CandidateSelectCourseForm()
    return render(request, "docencia/selectcourse.html", locals())
# <> fin selectCourse

def successStudent(request):
    student = StudentPersonalInformation.objects.get(pk=2)
    return render(request, "docencia/successtudent.html", locals())
# <> fin prueba


def courseList(request):
    if request.method == "POST":
        search_text = request.POST.get('search')

        response_data = {}

        data = serializers.serialize("json", CourseInformation.objects.
                                     filter(name__icontains=search_text).
                                     order_by('name')[:100])

        response_data["data"] = data

        return JsonResponse(response_data)
    else:
        _courses_total_ = CourseInformation.objects.all().order_by('name')

        courses_total = []

        for course in _courses_total_:
            course.groups = []
            for group in GroupInformation.objects.filter(course=course.pk):
                course.groups.append(group)
            courses_total.append(course)

        try:
            paginador = Paginator(courses_total, 100)
            page = request.GET.get('page')

            courses = paginador.get_page(page)
        except UnorderedObjectListWarning:
            paginador = []
            page = []

        return render(request, "docencia/listcourses.html", locals())
# <> fin listcourse


def candidateList(request, pk):

    course_name = CourseInformation.objects.get(pk=pk).name

    candidates = Candidate.objects.filter(course=pk)

    color = ["w3-teal", "w3-pink", "w3-purple", "w3-deep-purple", "w3-indigo", "w3-blue", "w3-lime", "w3-deep-orange"]

    return render(request, "docencia/listcandidate.html", locals())
# <> fin candidateList


@require_POST
def interviewCandidateAjax(request):
    candidatePk = request.POST.get("candidate")

    candidate = Candidate.objects.get(pk=candidatePk)
    candidate.interview = not candidate.interview
    candidate.save()

    if not candidate.interview:
        candidate.selected = False
        candidate.save()

    response_data = {"data": candidate.interview}

    return JsonResponse(response_data)
# <> fin interviewCandidateAjax


@require_POST
def recomendedCandidateAjax(request):
    candidatePk = request.POST.get("candidate")

    candidate = Candidate.objects.get(pk=candidatePk)
    candidate.recommended = not candidate.recommended
    candidate.save()

    response_data = {"data": candidate.recommended}

    return JsonResponse(response_data)
# <> fin interviewCandidateAjax


@require_POST
def selectedCandidateAjax(request):
    candidatePk = request.POST.get("candidate")

    candidate = Candidate.objects.get(pk=candidatePk)
    candidate.selected = not candidate.selected
    candidate.save()

    response_data = {"data": candidate.selected}

    return JsonResponse(response_data)
# <> fin interviewCandidateAjax


@require_POST
def manyCandidateAjax(request):
    cursePk= request.POST.get("course")

    candidate_interview = Candidate.objects.filter(course=cursePk, interview=True).__len__()
    candidate_selected = Candidate.objects.filter(course=cursePk, selected=True).__len__()
    candidate_recomended = Candidate.objects.filter(course=cursePk, recommended=True).__len__()

    response_data = {
        "interview": candidate_interview,
        "selected": candidate_selected,
        "recomended": candidate_recomended
    }

    return JsonResponse(response_data)
# <> fin selectedCandidateAjax


def candidateToGroup(request, pk):
    course_name = CourseInformation.objects.get(pk=pk).name

    candidates = Candidate.objects.filter(course=pk, selected=True)

    groups = GroupInformation.objects.filter(course=pk, current=True)

    studentsGroup = []
    for groupActive in groups:
        for student in GroupList.objects.filter(group=groupActive.pk):
            studentsGroup.append(student)

    return render(request, "docencia/candidateToGroup.html", locals())
# <> fin candidateToGroup


@require_POST
def candidateToGroupAjax(request):
    studentPk= request.POST.get("candidate")
    groupPk = request.POST.get("group")
    coursePk = request.POST.get("course")

    # verificar si el estudiante
    for groupActive in GroupInformation.objects.filter(course=coursePk, current=True):
        for studentGroupList in GroupList.objects.filter(student=studentPk, group=groupActive.pk):
            studentGroupList.delete()

    try:
        groupList = GroupList()
        groupList.student = Candidate.objects.get(pk=studentPk)
        groupList.group = GroupInformation.objects.get(pk=groupPk)
        groupList.save()
    except:
        pass

    response_data = {
        "data": "True",
    }

    return JsonResponse(response_data)
# <> fin candidateToGroupSelect


def assitence(request, pk):
    groupList = GroupList.objects.filter(group=pk)
    group = GroupInformation.objects.get(pk=pk)

    for i in range(groupList.__len__()):
        groupList[i].inasistencias = Assistence.objects.filter(
            assis_grouplist=groupList[i].pk, assis_status="i").__len__()

        groupList[i].tardanzas = Assistence.objects.filter(
            assis_grouplist=groupList[i].pk, assis_status="t").__len__()

    return render(request, "docencia/assistence.html", locals())
# <> fin assistenceView


@require_POST
def assistenceTakeAjax(request):
    groupListPk = request.POST.get("groupList")
    status = request.POST.get("status")

    fecha = datetime.datetime.today()
    fechaIni = datetime.datetime(fecha.year, fecha.month, fecha.day, 0, 0, 0)
    fechaFin = datetime.datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)

    print(fechaIni, fechaFin)

    for _assistence_ in Assistence.objects.filter(assis_grouplist=groupListPk, assis_dateTime__range=(fechaIni, fechaFin)):    
        print("\n\n>> Eliminando Registro de Asistencia " + _assistence_.__str__() + "\n\n")
        _assistence_.delete()

    assistence = Assistence()
    assistence.assis_grouplist = GroupList.objects.get(pk=groupListPk)
    assistence.assis_dateTime = datetime.datetime.now()
    assistence.assis_status = status
    assistence.save()

    print("\n\n>> " + assistence.__str__() + "\n\n")

    response_data = {
        "data": "True",
    }

    return JsonResponse(response_data)
# <> fin assistenceCheckAjax


@require_POST
def assistenceCheckAjax(request):
    fecha = datetime.datetime.today()
    fechaIni = datetime.datetime(fecha.year, fecha.month, fecha.day, 0, 0, 0)
    fechaFin = datetime.datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)

    groupListSal = []
    groupList = GroupList.objects.filter(group=request.POST.get('group'))

    for i in range(groupList.__len__()):
        try:
            asistencia = Assistence.objects.get(assis_grouplist=groupList[i].pk, assis_dateTime__range=(fechaIni, fechaFin))
        
            groupListSal.append(["%s" % groupList[i].pk, asistencia.assis_status])
        except:
            groupListSal.append(["%s" % groupList[i].pk, "0"])

    print(groupListSal)

    response_data = {
        "groupList": groupListSal,
    }

    return JsonResponse(response_data)    
# <> fin assistenceCheckAjax


@require_POST
def assistenceStatusAjax(request):
    groupListPk = request.POST.get('groupListPk')
    status = request.POST.get('status')

    assistence = []
    for _assistence_ in Assistence.objects.filter(assis_grouplist=groupListPk, assis_status=status).order_by('-dateTime'):
        assistence.append(_assistence_.assis_dateTime.strftime('%d/%m/%Y'))
    
    response_data = {
    'groupList': assistence
    }

    return JsonResponse(response_data)
# <> fin assistenceStatusAjax


def assistenceRasp(request, ci, rasp):

    candidate = Candidate.objects.filter(student__numberidentification=ci)
    if not candidate:
        return JsonResponse({'data': 'false'})

    print("\n", candidate, "\n")

    # Buscando el GroupList
    groupList = GroupList.objects.filter(
        group=GroupInformation.objects.get(classroom = Raspberrys.objects.get(name=rasp).classroom),
        student=Candidate.objects.get(student__numberidentification=ci)
    )

    fecha = datetime.datetime.today()
    fechaIni = datetime.datetime(fecha.year, fecha.month, fecha.day, 0, 0, 0)
    fechaFin = datetime.datetime(fecha.year, fecha.month, fecha.day, 23, 59, 59)

    print(fechaIni, fechaFin)

    for _assistence_ in Assistence.objects.filter(assis_grouplist=groupList.pk, assis_dateTime__range=(fechaIni, fechaFin)):    
        print("\n\n>> Eliminando Registro de Asistencia " + _assistence_.__str__() + "\n\n")
        _assistence_.delete()

    assistence = Assistence()
    assistence.assis_dateTime = datetime.datetime.now()
    assistence.assis_status = "a"
    assistence.assis_grouplist = groupList
    print(">>> Asistencia Auto " + assistence.__str__())
    # assistence.save()

    response_data = {
    'data': 'ok',
    }

    return JsonResponse(response_data)
# <> fin assistenceRasp
