from django.urls import path
from fvb_app import views
urlpatterns = [
    path('',views.stu_list),
    path('<int:pk>',views.stu_detail)

]
