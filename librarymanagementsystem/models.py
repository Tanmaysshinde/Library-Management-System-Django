from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_id = models.IntegerField()
    author = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.book_name) + " " + "["+ str(self.book_id)+ "]"

class students(models.Model):
    Name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    branch = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return str(self.Name) + " " + "["+ str(self.student_id)+ "]"
    
class Issuedbook(models.Model):
    book_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=50)
    book_id = models.IntegerField()
    student_id = models.CharField(max_length=50)
    student_phone_no = models.CharField(max_length=10)
    def __str__(self):
        return str(self.book_name )