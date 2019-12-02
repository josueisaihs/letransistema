from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StudentPersonalInformation, StudentPersonalInformation.Admin)
admin.site.register(TeacherPersonalInformation, TeacherPersonalInformation.Admin)
admin.site.register(CourseInformation, CourseInformation.Admin)
admin.site.register(GroupInformation, GroupInformation.Admin)
admin.site.register(GroupList, GroupList.Admin)
admin.site.register(Candidate, Candidate.Admin)
admin.site.register(ClassRoom, ClassRoom.Admin)
admin.site.register(Raspberrys, Raspberrys.Admin)
admin.site.register(Assistence, Assistence.Admin)
