from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = "__all__"


class CustomEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','emp_name', 'emp_dob', 'emp_email'] 