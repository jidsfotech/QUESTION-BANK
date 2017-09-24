from django.conf.urls import patterns, url
from Qbank import views
from django.conf import settings
from django.conf.urls.static import static



#url mapping for view functions
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^about/$', views.about, name='about'),
url(r'^login/$', views.user_login, name='login'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^changepassword/$', views.ChangePassword, name='changepassword'),
url(r'^levels/$',views.Levels, name='levels'),
url(r'^courses/(?P<sel_lev>\w+)/$', views.Courses, name='courses'),
url(r'^questions/(?P<sel_course>\w+)/$',views.Questions, name='questions'),
#url(r'^display/[\w.]+/(?P<file_name>[\w.-]+)/$', views.Display, name='display'),
url(r'^ajaxtest/$', views.ajaxtest, name='ajaxtest'),
url(r'^uploadQpapers/$', views.uploadQpapers, name='uploadQpapers'),
url(r'^getCourseCodeAndTitle/(?P<pri_key>[\w.-]+)/$', views.getCourseCodeAndTitle, name='getCourseCodeAndTitle'),
]

""" A regular expression for listing courses for any selected level, courses etc url(r'^pattern_name/(?P<parameter to be passed>\w+)/$', views.name_of_view_function, name ='pattern_name') """



    
     