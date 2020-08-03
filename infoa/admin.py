from django.contrib import admin

# Register your models here.
from .models import Employee, Benefit
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first','last','gender','start_date','end_date', 'email','emp_type', 'dept', 'position']

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    pass