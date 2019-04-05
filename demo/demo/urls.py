from django.contrib import admin
from django.conf.urls import url,include
from da import views
urlpatterns = [
    url('admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^da/',include('da.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
