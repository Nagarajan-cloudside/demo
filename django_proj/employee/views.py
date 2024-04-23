from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):

        
    def get_all_data(self, request, format=None):
        try:
            queryset = Employee.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response( serializer.data)
        except Exception as e:
            return Response({'error': str(e)})
    
    
    def post_data(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def get_data(self, request, pk= None):

        try:

            queryset = Employee.objects.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response (serializer.data )
        
        except Exception as e:
            return Response({'error ': str(e)}, status = status.HTTP_404_NOT_FOUND)

    def update_data(self, request, pk=None):
        try:
            queryset = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete_data(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response({f"{pk}": "deleted the record"})
       
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        

    
