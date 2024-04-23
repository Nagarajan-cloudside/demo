from django.db import models

# Create your models here.

class Employee(models.Model):
    
    emp_name = models.CharField(max_length=100, null = False)
    emp_email = models.EmailField(max_length=100, null = False)
    emp_phone = models.CharField(max_length=12, null = False)
    emp_dob = models.DateField()
    create_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.emp_name
    