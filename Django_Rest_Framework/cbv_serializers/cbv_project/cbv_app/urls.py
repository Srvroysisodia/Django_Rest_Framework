from cgitb import lookup
from django import views
from django.urls import path
from cbv_app import views
urlpatterns = [
    path('',views.Student_list.as_view()),
    path('<int:stu_id>',views.Student_details.as_view()),

]