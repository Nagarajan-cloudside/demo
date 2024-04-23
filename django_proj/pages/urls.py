from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet, basename = 'book')

urlpatterns = [
    path('books/', BookViewSet.as_view({'get':'list', 'post': 'create', }), name ="book-list"),
    path('books/<int:pk>', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='book-detail'),

    
]