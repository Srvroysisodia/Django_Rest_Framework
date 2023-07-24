from database.models import Emp_Details
from .serializers import EmpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
###ViewSets.ViewSet
from rest_framework import viewsets
###ViewSets.ModelViewSet
from rest_framework.viewsets import ModelViewSet
### GenericApiView Mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
### Concrete API View(GENERICS) ListApiView,PostApiView etc....
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView

#_______________________Class Based View ________________________________________________ 
######################## ViewSets.ViewSet#############################################################
class Empviewset(viewsets.ViewSet):
    def list(self,request):
        emp=Emp_Details.objects.all()
        serializer=EmpSerializer(emp,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            data=Emp_Details.objects.get(id=id)
            serializer=EmpSerializer(data)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg={"msg":"Data Created"}
            return Response(msg,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        id=pk
        if id is not None:
            id=Emp_Details.objects.get(id=id)
            serializer=EmpSerializer(id,data=request.data,partial=True)
            return Response(serializer.data)
    
    def delete(self,request,pk=None):
        id=pk
        if id is not None:
            id=Emp_Details.objects.get(id=id)
            id.delete()
            msg={"msg":"Data Deleted! "}
            return Response(msg,status=status.HTTP_202_ACCEPTED)

#_______________________Class Based View ________________________________________________ 
######################## ViewSets.ModelViewSet#############################################################
class EmpModelview(viewsets.ModelViewSet):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
#_______________________Class Based View ________________________________________________ 
######################## API View CRUD#############################################################
# Create your views here.
class EmpApiView(APIView):
    def get(self, request):
        data=Emp_Details.objects.all()
        serializer=EmpSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created"})
    
    def retrieve(self, request,pk=None):
        id=pk
        if id is not None:
            data=Emp_Details.objects.get(pk=id)
            serializer=EmpSerializer(data)
            return Response(serializer.data)
    def put(self, request,pk=None):
        id=pk
        if id is not None:
            data=Emp_Details.objects.get(pk=id)
            serializer=EmpSerializer(data,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
    def delete(self, request,pk=None):
        id=pk
        if id is not None:
            data=Emp_Details.objects.get(pk=id)
            data.delete()
            msg={"msg":"Deleted"}
            return Response(msg)
        
########################Generic API View CRUD (MIXINS)  #############################################################
#____________________________________________________________________________________________________________________________________________________________________________
class EmpListMixin(GenericAPIView,ListModelMixin):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class EmpPostMixin(GenericAPIView,CreateModelMixin):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class EmpRetrieveMixin(GenericAPIView,RetrieveModelMixin):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class EmpPutMixin(GenericAPIView,UpdateModelMixin):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class EmpDelMixin(GenericAPIView,DestroyModelMixin):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
        
    
########################Concrete View Class (Generics__ListApiView,PostApiView,UpateApiVew Etc..)  #############################################################
#____________________________________________________________________________________________________________________________________________________________________________
class EmpGenlist(ListAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
class EmpGenCreate(CreateAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer

class EmpGenUpdate(UpdateAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
class EmpGenRetrieve(RetrieveAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
class EmpGendelete(DestroyAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
class EmpGenListCreate(ListCreateAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
class EmpGenUpdateRetrieveDelete(RetrieveUpdateDestroyAPIView):
    queryset=Emp_Details.objects.all()
    serializer_class=EmpSerializer
    
    
