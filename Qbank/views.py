from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Qbank.models import *
from django.conf import settings
import os
import json 
from Qbank.FileSerializer import serialize_field
from django.core.serializers.json import DjangoJSONEncoder
from Qbank.forms import QuestionBankForm


# A call RequestContext class to gain access to settings related to the user’s request
from django.template import RequestContext

# A call to shortcuts class to gain acess to Render_to_response function
from django.shortcuts import render_to_response


def index(request): 
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    """ The render_to_response() function will take this data 
    and mash it together with the template to produce a complete HTML page """
    return render_to_response('Qbank/index.html', context_dict, context)
    
def about(request):
    context = RequestContext(request)
    context_dict = {'aboutmessage':'THIS IS THE ABOUT PAGE'}
    return render_to_response('Qbank/about.html', context_dict, context)
    
    
""" user_login() is used for authenticating users before serving them the question bank page """  
  
def user_login(request):
    context = RequestContext(request)

    #if the incoming request is a post request, the username and password are retrieved and test for validation
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #this line verifys the user credentials against inbuilt verification mechanism in the authenticate()
        user = authenticate(username=username, password=password)
        
        #if after verification the user exist and has an active account then the suer object is created and passed to Login().  
        if user is not None and user.is_active:
            
        #login() log the user in and redirect them to the appropriate page
            login(request, user)            
            return HttpResponseRedirect('/Qbank/levels/')
        else:
            messages.error(request, 'Invalid login details!.. please try again.')
            return render_to_response('Qbank/index.html', {}, context)
        
                  
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/Qbank/')
       
def Levels(request):
    context = RequestContext(request)
    
#this line quesries the ClassLevel model to retrieve all the stored class levels in (ClassLevel model)
    ClassLevel_List = ClassLevel.objects.all()
    
    context_dict = {'classlevel_list': ClassLevel_List}    
    
    return render_to_response('Qbank/LevelPage.html',context_dict, context)

   
   
def Courses(request, sel_lev):
    context = RequestContext(request)
    
#this line remove the '_' underscores in the name of the level selected
    SelectedLev = sel_lev.replace('_',' ')
    
    context_dict = {'selectedLev':SelectedLev}
    
    levPk = ClassLevel.objects.get(level=SelectedLev)
    CourseToDisp = CourseRecord.objects.filter(level = levPk.id )
    
    context_dict['CourseToDisp'] = CourseToDisp

    return render_to_response('Qbank/CoursesPage.html',context_dict, context)
    
 
""" this function accepts argument provided in the url to query and display all the available question papers for a particular course""" 

def Questions(request, sel_course):
   
    SelCourse = sel_course.replace('_',' ')
    
    if request.is_ajax(): 
    
        QuestionPapaers = QuestionBank.objects.filter(CourseCode=SelCourse).values_list('question_papers','Semester','CourseUnit','Date','CourseTitle')
        
        json_list_QuestionPapers = json.dumps(list(QuestionPapaers), cls=DjangoJSONEncoder)
        return HttpResponse(json_list_QuestionPapers)
    
def Display(request, file_name):

     
    File_Name = file_name.replace('_', ' ')
    file_path = os.path.join(settings.MEDIA_ROOT, 'QuestionPapers',File_Name)
    
   
    return file_path
    
def ajaxtest(request):
    context = RequestContext(request)
    return render_to_response("Qbank/AjaxTest.html", {}, context)

def uploadQpapers(request):
    context = RequestContext(request)
    Qpapers = QuestionBankForm(request.POST, request.FILES)
    if request.method == 'POST':
       if Qpapers.is_valid():
           
           Upload_Qpapers = Qpapers.save(commit=False)
           
           if 'question_papers' in request.FILES:
               Upload_Qpapers.question_papers = request.FILES['question_papers']
               Qpapers.save()
               messages.success(request, 'Question paper was successfully uploaded!.')
               return redirect('/Qbank/uploadQpapers/')
       else:
           messages.success(request, 'Invalid inputs make sure you feel all the necessary informations.')
           Qpapers = QuestionBankForm()
           return render_to_response("Qbank/uploadQpapers.html", {'Qpapers':Qpapers}, context)
        
    else:
        Qpapers = QuestionBankForm()
        return render_to_response("Qbank/uploadQpapers.html", {'Qpapers':Qpapers}, context)
        
                                  
    
def getCourseCodeAndTitle(request, pri_key):
    Pri_key = pri_key.replace('_',' ')
    
    if request.is_ajax:
        course = ClassLevel.objects.get(pk=Pri_key)
        list_course = CourseRecord.objects.filter(level=course).values_list('Course_Title', 'Course_Code')
        
        json_list_course = json.dumps(list(list_course), cls=DjangoJSONEncoder)
        return HttpResponse( json_list_course)
        
def ChangePassword(request):
    context = RequestContext(request)
    if request.method == 'POST':
        ChangePswd = PasswordChangeForm(request.user, request.POST)
        if ChangePswd.is_valid():
            user = ChangePswd.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was succesfully updated')
            return redirect('/Qbank/levels/')
        else:
            messages.error(request, 'Please correct the errors below!...')

    else:
        ChangePswd = PasswordChangeForm(request.user)
    return render_to_response("Qbank/PasswordChangeForm.html", {'ChangePswd':ChangePswd}, context)
    
                        
        
        

       
    
 

    
    

        
        

    
    
            
        
	
    
