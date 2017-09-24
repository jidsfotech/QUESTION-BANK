

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import date





class UserProfile (models.Model):

# This line is required. Links UserProfile to a User model instance
    user = models.OneToOneField(User)

# The additional attributes we wish to include to the User Model.    
    lecturer ='Lecturer'
    student ='Student'
    status = 'Admin'
    
    User_Category = ((status,'Admin'),(lecturer, 'Lecturer'),(student, 'Student'))
    Account_Type = models.CharField(max_length =20, choices =User_Category, default = status)
    
    Upload_Picture = models.ImageField(upload_to = 'profile_images', blank = True)
        
    def __str__(self):
        return self.user.username
        
""" this is the class level and question bank model"""    
class ClassLevel(models.Model):
    level = models.CharField(max_length=100, unique=True)

#this line returns the specified attributes of the models object when queried   
    def __str__(self):
        return self.level
        
class CourseRecord(models.Model):
    First_Semester ='First_Semester'
    Second_Semester ='Second_Semester'
    Semesters = ((First_Semester, 'First_Semester'),(Second_Semester, 'Second_Semester'))
    
    level = models.ForeignKey(ClassLevel)
    Course_Title = models.CharField(max_length=50, null=False,unique=True)
    Course_Code = models.CharField(max_length=10, null=False, unique=True)
    Course_Unit = models.PositiveSmallIntegerField()
    Semester = models.CharField(max_length=20, choices=Semesters, default="Select_Semester", )
    
    def __str__(self):
        return '%s %s %s %s %s' %(self.Course_Title, self.Course_Code, self.Course_Unit, self.Semester, self.level)
    

     
class QuestionBank(models.Model):

    First_Semester ='First_Semester'
    Second_Semester ='Second_Semester'
    Semesters = ((First_Semester, 'First_Semester'),(Second_Semester, 'Second_Semester'))
    
    level = models.ForeignKey(ClassLevel)
    CourseTitle = models.CharField(max_length=50, null=False)
    CourseCode = models.CharField(max_length=10, null=False )
    CourseUnit = models.IntegerField()
    Semester = models.CharField(max_length=20, choices=Semesters, default="Select_Semester")
    Date = models.DateField()
    question_papers = models.FileField(upload_to = 'QuestionPapers')

#this line returns the specified attributes of the models object when queried    
    def __str__(self):
        return '%s %s %s %s %s %s %s' %(self.level, self.CourseTitle, self.CourseCode, self.CourseUnit, self.Semester, self.Date, self.question_papers )

