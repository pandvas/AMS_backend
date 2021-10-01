from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=400)

    username=None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.name

class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Department(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Hod(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    id_hod=models.OneToOneField(Department,on_delete=models.CASCADE)
    address=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    designation=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    address=models.CharField(max_length=30)
    contactdetails=models.CharField(max_length=60)
    yearofpassing=models.IntegerField()

    def __unicode__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    departmentid=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    date=models.DateField()
    venue=models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Eventpoll(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    interested=models.BooleanField(default=True)

    def __unicode__(self):
        return self.interested

class StudentPassword(models.Model):
    id = models.AutoField(primary_key=True)
    studentid=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __unicode__(self):
        return self.password

class Contact(models.Model):
    name = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    email =models.EmailField(primary_key=True)

    def __unicode__(self):
        return self.name




#---------------------------------Mapper------------------------------------------------

class Department_mapper(models.Model):
    id=models.AutoField(primary_key=True)
    departmentid=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    universityid=models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)
    hodid=models.ForeignKey(Hod,on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.departmentid

class Faculty_mapper(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,blank=True)
    departmentid=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    universityid=models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.facultyid

class Student_mapper(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    courseid=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    universityid=models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)
    departmentid=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.studentid

class Rollno_mapper(models.Model):
    id = models.AutoField(primary_key=True)
    rollno=models.IntegerField()
    studentid=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)

    def __unicode__(self):
        return self.rollno

class Event_mapper(models.Model):
    id = models.AutoField(primary_key=True)
    eventid=models.ForeignKey(Event,on_delete=models.CASCADE,null=True,blank=True)
    departmentid=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.eventit

class Poll2(models.Model):
    option = models.CharField(max_length=30)