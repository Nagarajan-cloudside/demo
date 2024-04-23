from django.urls import path, include
from .views import EmployeeViewSet

urlpatterns = [
    path("employee/", EmployeeViewSet.as_view({'get':'get_all_data', 'post' : 'post_data'}), name = 'employee-list'),
    path('employee/<int:pk>/', EmployeeViewSet.as_view({ 'get': "get_data", 'put': "update_data", 'delete' : 'delete_data'}), name =  "employee-details"),


]

