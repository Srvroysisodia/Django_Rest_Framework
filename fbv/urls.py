from django.urls import  path
from .views import stulist,stucreate,crud_fxn
urlpatterns=[
    path('list',stulist,name='list_method'),
    path('create',stucreate,name='create_method'),
    path('crud/',crud_fxn,name='crud'),
    path('crud/<int:pk>',crud_fxn,name='crudid'),
    
    ]