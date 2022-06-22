from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

context = {}

def loginform():
    login_form = login_Form()
    context['loginform'] = login_form

def admin_login(request):
    if not request.user.is_authenticated:
        loginform()
        if request.POST.get('username') != None:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                print(username, user)
                if user is not None:
                    request.session['user'] = username
                    auth.login(request, user)
                    return redirect('adminpanel')
                else:
                    messages.error(request, "Invalid Credentials!!")
        return render(request, 'adminlogin.html', context)
    else:
        return redirect('adminpanel')

def logout(request):
    try:
        del request.session['user']
    except:
        pass
    request.session.flush()
    request.session.clear_expired()
    auth.logout(request)
    return redirect('home')

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('adminpanel')

@login_required(login_url='adminLogin')
def adminsuccess(request):  
    return render(request, 'admin.html')

@login_required(login_url='adminLogin')
def adaddnewbooks(request):
    newbook = Add_newBooks()
    books = Books()
    context['newbook'] = newbook
    if request.method == 'POST':
        books.book_name = request.POST['book_name']
        books.book_id = request.POST['book_id']
        books.author = request.POST['author']
        books.quantity = request.POST['quantity']
        books.save()
        messages.info(request, "New Book Added!!")
    return render(request, 'addnewBooks.html', context)

@login_required(login_url='adminLogin')
def viewbooks(request):
    books = Books.objects.all()
    context['books'] = books
    return render(request, 'viewbooks.html', context)

def deletebook(request):
    book = Books.objects.get(id = request.GET.get('id'))
    book.delete()
    messages.info(request, "Book Deleted Succesfully!!")
    return redirect('viewbooks')

@login_required(login_url='adminLogin')
def editbook(request):
    newbook = Add_newBooks()
    context['newbook'] = newbook
    book = Books.objects.get(pk = request.GET.get('id'))
    context['book'] = book
    if request.method == 'POST':
        book.book_name = request.POST['book_name']
        book.book_id = request.POST['book_id']
        book.author = request.POST['author']
        book.quantity = request.POST['quantity']
        book.save()
        messages.info(request, "Book Edited Successfully!!")
        return redirect('viewbooks')
    return render(request, 'editbook.html', context)

@login_required(login_url='adminLogin')
def addStudent(request):
    newstudent = Add_newstudent()
    student = students()
    context['newstudent'] = newstudent
    if request.method == 'POST':
        student.Name = request.POST['Name']
        student.student_id = request.POST['student_id']
        student.branch = request.POST['branch']
        student.phone_no = request.POST['phone_no']
        student.email = request.POST['email']
        student.save()
        messages.info(request, "New Student Added!!")
    return render(request, 'addstudent.html', context)

@login_required(login_url='adminLogin')
def viewstudents(request):
    student = students.objects.all()
    context['students'] = student
    return render(request, 'viewstudents.html', context)

@login_required(login_url='adminLogin')
def editstudent(request):
    newstudent = Add_newstudent()
    context['newstudent'] = newstudent
    student = students.objects.get(pk = request.GET.get('id'))
    context['student'] = student
    if request.method == 'POST':
        student.Name = request.POST['Name']
        student.student_id = request.POST['student_id']
        student.branch = request.POST['branch']
        student.phone_no = request.POST['phone_no']
        student.email = request.POST['email']
        student.save()
        messages.info(request, "Student Edited Successfully!!")
        return redirect('viewstudents')
    return render(request, 'editstudent.html', context)

def deletestudent(request):
    student = students.objects.get(id = request.GET.get('id'))
    student.delete()
    messages.info(request, "Student Deleted Succesfully!!")
    return redirect('viewstudents')

@login_required(login_url='adminLogin')
def issue_book(request):
    issuedbook = issuebook()
    issuedbooks = Issuedbook()
    context['issuebook'] = issuedbook
    if request.method == 'POST':
        book_id = request.POST['book_name']
        book = Books.objects.get(pk = book_id)
        student_id = request.POST['student_name']
        student = students.objects.get(pk = student_id)
        book.quantity -= 1
        issuedbooks.book_name = book.book_name
        issuedbooks.student_name = student.Name
        issuedbooks.book_id = book.book_id
        issuedbooks.student_id = student.student_id
        issuedbooks.student_phone_no = student.phone_no
        issuedbooks.save()
        book.save()
        messages.info(request, "Book Issued Succesfully!!")
    return render(request, 'issuebook.html', context)

@login_required(login_url='adminLogin')
def viewissuedbooks(request):
    issuedbook = Issuedbook.objects.all()
    context['issuedbooks'] = issuedbook
    return render(request, 'viewissuedbooks.html', context)

def returnIssuedBook(request):
    issuedbook = Issuedbook.objects.get(id = request.GET.get('id'))
    book = Books.objects.get(book_name = issuedbook)
    book.quantity +=1
    book.save()
    issuedbook.delete()
    messages.info(request, "Book Return Succesfully!!")
    return redirect('viewissuedbooks')
    
def student(request):
    books = Books.objects.all()
    context['books'] = books
    return render(request, 'student.html', context)