from django.db import models

# Create your models here.

#Creating Company Model




class Company(models.Model):
    company_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about=models.TextField()
    type = models.CharField(max_length=50, choices=(('IT', 'IT'), ('OPC', 'OPC'), ('Fintech', 'Fintech ')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


#Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    position=models.CharField(max_length=100, choices=(
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Intern', 'Intern'),
    ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)   #One to many relations with the company