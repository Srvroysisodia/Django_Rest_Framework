from django.urls import path,include
from .views import EmpApiView,EmpListMixin,EmpPostMixin,EmpRetrieveMixin,EmpPutMixin,EmpDelMixin,EmpGenlist,EmpGenCreate,EmpGenUpdate,EmpGendelete,EmpGenListCreate,EmpGenUpdateRetrieveDelete,EmpGenRetrieve,Empviewset,EmpModelview

###As its Class Based Function So in url We have to put as_view(),
# because url resolver knows function only

###Using Default Router For Viewset & ModelViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router1=DefaultRouter()
router.register('empviewset',Empviewset,basename='emp')
router1.register('empmodel',EmpModelview,basename='emp')

urlpatterns=[
    ###Viewsets.Viewset
    path('',include(router.urls)),
    path('',include(router1.urls)),
    
    #####API VIEW ######
    path('apiview',EmpApiView.as_view(),),
    
    #### GenericModelApiView MIxins ######
    path('cbv/list',EmpListMixin.as_view(),name='list'),
    path('cbv/create',EmpPostMixin.as_view(),name='create'),
    path('cbv/retrieve/<int:pk>',EmpRetrieveMixin.as_view()),
    path('cbv/update/<int:pk>',EmpPutMixin.as_view()),
    path('cbv/delete/<int:pk>',EmpDelMixin.as_view()),
    
    #### GenericModelApiView MIxins ######
    path('cbv/gen/list',EmpGenlist.as_view(),name='list'),
    path('cbv/gen/create',EmpGenCreate.as_view(),name='create'),
    path('cbv/gen/retrieve/<int:pk>',EmpGenRetrieve.as_view()),
    path('cbv/gen/update/<int:pk>',EmpGenUpdate.as_view()),
    path('cbv/gen/delete/<int:pk>',EmpGendelete.as_view()),
    path('cbv/gen/list-create',EmpGenListCreate.as_view()),
    path('cbv/gen/upd-ret-del/<int:pk>',EmpGenUpdateRetrieveDelete.as_view()),
    
    
    
    ]