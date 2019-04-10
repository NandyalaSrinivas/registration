from django.conf.urls import url

from . import views

app_name = 'studentinfo'

urlpatterns = [
        url(r'index/$', views.index, name='index'),
        url(r'^create/$', views.create_registration, name='create'),
        url(r'^(?P<registration_id>[0-9]+)/detail/$', views.student_detail, name='student_detail'),
        url(r'login/$', views.user_login, name='user_login'),
        url(r'password/$', views.user_regisration, name='password'),
        url(r'logout/$', views.user_logout, name='user_logout'),



]
