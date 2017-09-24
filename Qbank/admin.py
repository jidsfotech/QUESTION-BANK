from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from Qbank.models import *


""" this class is use to customise the admin site """
class User_profileInline(admin.StackedInline):
    model = UserProfile 
    candelete = False
    verbose_name_plural = 'UserProfile'

""" this class is use to customise the admin site to display  UserProfile model in in the admin interface"""
class UserAdmin(UserAdmin):
    inlines = (User_profileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'User_Status')
    list_select_related = ('userprofile',)
    
    def User_Status(self, instance):
        return instance.userprofile.Account_Type
        User_Status.short_description = "Account_Type"
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ClassLevel)
   
class CourseRecordAdmin(admin.ModelAdmin):
    list_display =('level','Course_Title', 'Course_Code', 'Course_Unit', 'Semester')
    


""" the following lines of code cutomise the way QuestionBank model is being displayed on the admin interface"""
class QuestionBankAdmin(admin.ModelAdmin):
    
   list_display =('level','CourseTitle', 'CourseCode', 'CourseUnit', 'Semester', 'Date', 'question_papers')
    
    
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(CourseRecord, CourseRecordAdmin)


# Register your models here.
