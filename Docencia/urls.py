from django.urls import path
from . import views



__author__ = "Josue Isai Hernandez Sanchez"
__email__ = "josueisaihs@gmail.com"

urlpatterns = [
    # Pagina Principal
    path('index/', views.userhome, name="view_index"),

    # Profesores
    path("newteacher/", views.teacherPersonalInformation, name='view_newteacher'),
    path("detailteacher/<int:pk>/", views.teacherDetail, name='view_detailteacher'),
    path("listteacher/", views.teacherList, name='view_listteacher'),
    path("editteacher/<int:pk>/", views.teacherEdit, name='view_editteacher'),
    path("delteacher/<int:pk>/", views.teacherDelete, name='view_delteacher'),
    

    # Estudiantes
    path("newstudent/", views.studentPersonalInformation, name='view_newstudent'),
    path("delstudent/<int:pk>/", views.studentDelete, name='view_delstudent'),
    path("editstudent/<int:pk>/", views.studentEdit, name='view_editstudent'),
    path("liststudent/", views.studentList, name='view_liststudent'),
    path("carnetstudent/<int:pk>", views.studentCarnet, name='view_studentCarnet'),
    path("carnetsstudents/<int:pk>", views.studentsCarnets, name='view_studentsCarnets'),

    # Cursos
    path("newcourse/", views.courseInformation, name='view_newcourse'),
    path("delcourse/<int:pk>", views.courseDelete, name="view_delcourse"),
    path("editcourse/<int:pk>", views.courseEdit, name="view_editcourse"),
    path("newgroup/", views.groupInformation, name='view_newgroup'),
    path("selectcourse/<int:pk>", views.selectCourse, name='view_selectcourse'),
    path("listcourses/", views.courseList, name="view_listcourses"),

    # Pruebas
    path("success/", views.successStudent, name="view_success"),

    # Grupos
    path("newgroup/", views.groupInformation, name='view_newgroup'),

    # Matricula
    path("enrollment/", views.indexEnrollment, name='view_enrollment'),

    # Candidatos Control
    path("candidate/<int:pk>", views.candidateList, name='view_candidates'),
    path("candidate/interview", views.interviewCandidateAjax, name='view_candidate_interview'),
    path("candidate/recomended", views.recomendedCandidateAjax, name='view_candidate_recomended'),
    path("candidate/selected", views.selectedCandidateAjax, name='view_candidate_selected'),
    path("candidate/many", views.manyCandidateAjax, name='view_candidate_many'),
    path("candidate/group/<int:pk>", views.candidateToGroup, name='view_candidate_to_group'),
    path("candidate/group/list", views.candidateToGroupAjax, name='view_candidate_to_group_select'),

    # Asistencia
    path("grouplist/assistence/<int:pk>", views.assitence, 
    name="view_assistence"),
    path("grouplist/assistence/change", views.assistenceTakeAjax, name="view_assistence_change"),
    path("grouplist/assistence/check", views.assistenceCheckAjax,
    name="view_assistence_check"),
    path('grouplist/assistence/status', views.assistenceStatusAjax, name='view_assistence_status'),
]

