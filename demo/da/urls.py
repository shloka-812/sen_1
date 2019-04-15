from django.conf.urls import url
from da import views
# SET THE NAMESPACE!
app_name = 'da'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^register_p/$',views.register_p,name='register_p'),
    url(r'^register_h/$',views.register_h,name='register_h'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^help/$', views.help, name='help'),
    url(r'^keyfacts/$', views.keyfacts, name='keyfacts'),
    url(r'^newsfeed/$', views.newsfeed, name='newsfeed'),
    url(r'^outbreaks/$', views.outbreaks, name='outbreaks'),
    url(r'^prediction/$', views.prediction, name='prediction'),
    url(r'^feeddata/$', views.feeddata, name='feeddata'),
    url(r'^outbreak_submission/$',views.outbreak_submission,name='outbreak_submission'),
             
]
