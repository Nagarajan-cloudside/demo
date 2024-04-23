from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from .models import Employee
from .serializers import EmployeeSerializer, CustomEmployeeSerializer
from rest_framework.decorators import action
from datetime import datetime

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # @action(detail=False, methods=['get'])
    def get_all_data(self, request, format=None):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})

    # @action(detail=False, methods=['get'], serializer_class=EmployeeSerializer)
    # def get_all_data(self, request, format=None):
    #     try:
    #         queryset = Employee.objects.all()
    #         serializer = EmployeeSerializer(queryset, many=True)
    #         return Response( serializer.data)
    #     except Exception as e:
    #         return Response({'error': str(e)})
    
    def post_data(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_data(self, request, pk= None):

        try:

            queryset = self.filter_queryset(self.get_queryset())
            employee = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(employee)
            return Response (serializer.data )
        
        except Exception as e:
            return Response({'error ': str(e)}, status = status.HTTP_404_NOT_FOUND)

    def update_data(self, request, pk=None):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            employee = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch_data(self, request, pk=None):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            employee = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(employee, data=request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete_data(self, request, pk=None):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            employee = get_object_or_404(queryset, pk=pk)
            employee.delete()
            return Response({f"{pk}": "deleted the record"})
       
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def head(self, request):
        """
        Handle HEAD requests.
        """
        return self.get_all_data(request)
    
    
    @action(detail=False, methods=['options'])
    def options(self, request):
        # Implement your logic to handle OPTIONS request
        # This method should return a response with allowed HTTP methods and any other relevant information
        return Response({'message': 'OPTIONS request handled successfully'}, status=status.HTTP_200_OK)
        



    def display(self, request):
        return Response("hello")
    


class CustomEmployeeViewSet(viewsets.ModelViewSet):
    

    queryset = Employee.objects.all()
    serializer_class = CustomEmployeeSerializer  # Define the serializer class attribute

    def validation_data(self, request, name=None):
        try:
            queryset = self.get_queryset.filter(emp_name__startswith=name)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)})

    def validation_two(self, request, name=None, email=None):
        name = request.query_params.get('name','')
        email = request.query_params.get('email','')

        try: 
            queryset = self.get_queryset(emp_name =name, emp_email = email)
            serializer = self.get.serializer(queryset)
            return   Response(serializer.data)
        except ExceptionGroup as e:
            return Response({'error' : str(e)})
        