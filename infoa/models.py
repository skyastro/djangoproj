from django.db import models

# Create your models here.
# Creating our class to cotain the required information for/about each employee
class Employee(models.Model):
    # first field for saving the first name
    first = models.CharField(max_length=40)
    # last field for saving the last name
    last = models.CharField(max_length=40)
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = models.CharField("Gender",max_length=1, choices=GENDER_CHOICES, blank=True)
    start_date = models.DateField("Start Date", blank=True)
    end_date = models.DateField("End Date", blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=12, blank=True)
    email = models.EmailField("Email", max_length=30, null=True, unique= True)
    EMP_TYPE = [("P","Part Time"),("F","Full TIme")]
    emp_type = models.CharField("Employment Type",max_length=1, choices=EMP_TYPE, blank=True)
    dept = models.CharField("Department",max_length=20, blank=True)
    position = models.CharField("Position",max_length=40, blank=True)
    benefits = models.ManyToManyField("Benefit", blank=True)
    
    def __str__(self):
        return (f"{self.first} {self.last}")


class Benefit(models.Model):
    # In this class we need to know just the name of each conference that the staff has:
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
