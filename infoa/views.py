# the render module will be used to render our html templates
from django.shortcuts import render
# Create your views here.
from .models import Employee
from django.http import Http404

# Any html page (template) you want to display/render has to have its own function defined in this file "views.py":

# starting with the first page "home page"
# def home ==> for the home page
# As a rule, every view function below has to have an argument called "request"
def home(request): # it takes a "request" as an argument, we can set the parameter as request
    # render(request: HttpRequest, template_name, { could be empty OR anything we want to pass to this page } )
    # { }
    # { 'feild1': numeric_value, 'feild2': 'text_value', 'field3': variable_name }
    employees = Employee.objects.all()
    return render(request,'home.html',{'employees':employees})

# def emp_detail ==> for the employee detail page
# this function requires the emp_id as a second parameter
def emp_detail(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        raise Http404('Sorry, Employee not found!')
    return render(request,'emp_detail.html',{'employee':employee})

# def about ==> for the about the project page
# about function has the required argument "request" and so on for all the functions
def about(request):
    return render(request,'about.html')
