from django.urls import path, include
from .views import EmployeeViewSet, CustomEmployeeViewSet

urlpatterns = [
    path("users/", EmployeeViewSet.as_view({'get':'get_all_data', 'post' : 'post_data' }), name = 'user-list'),
    path('', EmployeeViewSet.as_view(actions= {'get': 'display'}), name= 'welcome'),
    path('users/<int:pk>', EmployeeViewSet.as_view({ 'get': "get_data", 'put': "update_data", 'delete' : 'delete_data', 'patch': 'patch_data'}), name =  "employee-details"),
    path('users/', CustomEmployeeViewSet.as_view({'get': 'validation_data', 'get': 'validation_two'}), name = "validation"),
   
]

