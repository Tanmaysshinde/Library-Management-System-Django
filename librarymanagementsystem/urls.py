from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name=''),
    path('home', index, name='home'),
    path('student', student, name='student'),
    path('adlogin', admin_login, name="adminLogin"),
    path('adminpanel', adminsuccess, name="adminpanel"),
    path('adminpanel/adaddnewbooks', adaddnewbooks, name="adaddnewbooks"),
    path('adminpanel/viewbooks', viewbooks, name="viewbooks"),
    path('adminpanel/deletebook', deletebook, name="deletebook"),
    path('adminpanel/editbook', editbook, name="editbook"),
    path('adminpanel/addstudent', addStudent, name='addstudent'),
    path('adminpanel/viewstudents', viewstudents, name="viewstudents"),
    path('adminpanel/editstudent', editstudent, name="editstudent"),
    path('adminpanel/deletestudent', deletestudent, name="deletestudent"),
    path('adminpanel/issuebook', issue_book, name="issuebook"),
    path('adminpanel/viewissuedbooks', viewissuedbooks, name="viewissuedbooks"),
    path('adminpanel/returnissuedbook', returnIssuedBook, name="returnissuedbook"),
    path('logout', logout, name='logout'),
]