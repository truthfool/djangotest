from django.urls import path
from form_app import views

urlpatterns=[path(' ',views.student,name='index')]
