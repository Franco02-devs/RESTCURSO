from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.base.api import GeneralListApiView
from apps.records.api.serializers.general_serializers import LocationSerializer
from apps.records.models import Location

class LocationViewset( viewsets.GenericViewSet):
    serializer_class=LocationSerializer
    model=Location
    
    def get_queryset(self):
        return self.get_serializer().Meta().model.objects.filter(state=True)
    
    def get_object(self):
        return self.get_serializer().Meta().model.objects.filter(id=self.kwargs['pk'],state=True)
        
    def list(self, request):
        data= self.get_queryset()
        data= self.get_serializer(data, many=True)
        return Response(data.data)
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro correcto'}, status=status.HTTP_200_OK)
        return Response({'message':'','error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_object().exists():   
            serializer=self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Registro actualizado!'}, status=status.HTTP_200_OK)    
        return Response({'message': '','error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        if self.get_object().exists():
            self.get_object().get().state=False
            return Response({'message': 'Registro eliminado!'}, status=status.HTTP_200_OK)  
        return Response({'message': '','error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            
            
              
