
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from users import views
# from .views import complaint,contact,EventGet,Studentlist,eventUpdate,studentUpdate,Universitydelete,Universityupdate,FacuiltytGet,Roll_list,departmentUpdate,departmentSetDel,Registerget,Registerget,login,RegisterView,LoginView,UserView,LogoutView,RegisterUniversityView, RegisterDepartmentView,RegisterHodView, RegisterFacultyView, RegisterStudentView, RegisterCourseView, RegisterEventView, EventpollView, StudentPasswordView, ContactView, DepartmentMapperView, FacultyMapperView, StudentMapperView, RollNoMapperView, EventMapperView, Departmentlist, Universitylist, Hodlist
from users.views import *

urlpatterns = [
    path('admin/register/', RegisterView.as_view(),name="regit"),
    # path('admin/loginform/',LoginView.as_view()),
    path('admin/login/', LoginView.as_view(),name="login"),

    path('admin/', UserView.as_view()),
    path('admin/logout/', LogoutView.as_view()),
    path('admin/addUniversity/',RegisterUniversityView.as_view()),

    path('admin/addDepartment/', RegisterDepartmentView.as_view(),name="regdepart"),
    path('admin/addHod/', RegisterHodView.as_view(),name='hodreg'),
    path('admin/addFaculty/', RegisterFacultyView.as_view(),name='regfaculty'),
    path('admin/addStudent/', RegisterStudentView.as_view(),name='regstudent'),
    path('admin/addCourse/', RegisterCourseView.as_view(),name='regcourse'),
    path('admin/addEvent/', RegisterEventView.as_view(),name='eventreg'),

    path('eventPoll/', EventpollView.as_view()),

    path('studentPassword/', StudentPasswordView.as_view(),name='stpass'),
    path('contact/', ContactView.as_view(),name="ctrd"),

    path('admin/departmentMapper/', DepartmentMapperView.as_view()),
    path('admin/facultyMapper/', FacultyMapperView.as_view()),
    path('admin/studentMapper/', StudentMapperView.as_view()),
    path('admin/rollNoMapper/', RollNoMapperView.as_view()),
    path('admin/eventMapper/', EventMapperView.as_view()),
    path('getDepartment/', Departmentlist.as_view()),
    path('getUniversity/',Universitylist.as_view()),
    path('getHod/',Hodlist.as_view()),
    path('getfacuilty/', FacuiltytGet.as_view()),

    path('getStudent/',Studentlist.as_view()),
    path('getevent/',EventGet.as_view()),
    path('getRoll/',Roll_list.as_view()),

    path("ptup/<int:id>",views.UserViewSet3.as_view(),name="sdes"),
    path("ptdel/<int:id>",views.UserViewSetDel.as_view(),name="sd"),

    path("departup/<int:id>",views.departmentUpdate.as_view(),name="departUpdate"), 
    path("departdel/<int:id>",views.departmentSetDel.as_view(),name="sdes"),  

    path("universitydel/<int:id>",views.Universitydelete.as_view(),name="sdes"),  
    path("universityup/<int:id>",views.Universityupdate.as_view(),name="departUpdate"),

    path("eventup/<int:id>",views.eventUpdate.as_view(),name="departUpdate"),

    path("studentdel/<int:id>",views.StudentDel.as_view(),name="studel"),
    path("eventdel/<int:id>",views.EventDel.as_view(),name="edel"),

    path("studentup/<int:id>",views.studentUpdate.as_view(),name="departUpdate"),
    path("ppp2", views.poll2view.as_view()),
]
