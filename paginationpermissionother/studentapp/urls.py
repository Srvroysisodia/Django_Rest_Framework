from django.urls import path
from .views import StudentCreateListApiView,StudentRetUpdDestroyApiView

urlpatterns=[
    path('create-list',StudentCreateListApiView.as_view(),name='create-list'),
    path('ret-upd-des/<int:pk>',StudentRetUpdDestroyApiView.as_view(),name='ret-upd-des')
]