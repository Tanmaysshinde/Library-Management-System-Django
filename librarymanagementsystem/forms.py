from django import forms
from .models import *

class login_Form(forms.Form):

    username = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'id' : 'user_name',
                                                 'autocomplete': 'username',
                                                 'class' : 'form-control',
                                                 'placeholder' : 'Username',}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'password',
                                                    'autocomplete': 'password', 
                                                    'class' : 'form-control', 
                                                    'placeholder' : 'Password',}))

class Add_newBooks(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'id': 'book_name',
                                                'class': 'form-control',
                                                'placeholder': 'Enter Name of Book'}),
            'book_id': forms.TextInput(attrs={'id': 'book_id',
                                                'class': 'form-control',
                                                'placeholder': 'Enter ID of Book'}),
            'author': forms.TextInput(attrs={'id': 'author',
                                                'class': 'form-control',
                                                'placeholder': 'Enter Name of Author of the Book'}),
            'quantity': forms.NumberInput(attrs={'id': 'quantity',
                                                'class': 'form-control',
                                                'placeholder': 'Enter Quantity of the Books'})
        }

class Add_newstudent(forms.ModelForm):
    branch = forms.ChoiceField(choices=(('ME', 'Mechanical'),
                                        ('CS', 'Computer'),
                                        ('EXTC', 'Electronic'),
                                        ('CE', 'Chemical'),
                                        ('IT', 'Information Technology'),
                                        ('BSc IT', 'BSc IT'),
                                        ('BSc CS', 'BSc CS'),
                                        ('Bcom', 'Bcom'),
                                        ('BArch', 'BAech'),
                                        ('BSc', 'BSc')),
                                        widget= forms.Select(attrs={'id': 'student_branch',
                                                                    'class': 'form-control',
                                                                    'placeholder': 'Select branch of the Student'}))

    class Meta:
        model = students
        exclude = ('branch',)
        widgets = {
            'Name': forms.TextInput(attrs={'id': 'name',
                                                'class': 'form-control',
                                                'placeholder': 'Enter name of the Student'}),
            'student_id': forms.TextInput(attrs={'id': 'student_id',
                                                'class': 'form-control',
                                                'placeholder': 'Enter ID of the Student'}),
            'phone_no': forms.TextInput(attrs={'id': 'phone_no',
                                                'class': 'form-control',
                                                'placeholder': 'Enter Phone No. of the Student'}),
            'email': forms.EmailInput(attrs={'id': 'email',
                                             'class': 'form-control',
                                             'placeholder': 'Enter Email Id of Student'})
        }

class issuebook(forms.Form):
    student_name = forms.ModelChoiceField(queryset=students.objects.all(), empty_label='Select Name of Student', widget=forms.Select(attrs={'id': 'studentname',
                                                                                                    'class': 'form-control',}))
    book_name = forms.ModelChoiceField(queryset=Books.objects.all(), empty_label='Select Name of Book', widget=forms.Select(attrs={'id': 'issuebookname',
                                                                                                    'class': 'form-control',}))