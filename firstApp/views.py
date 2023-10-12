from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import *

def employeeView(request):
    emp = {
        'id' : 123,
        'name' : 'John',
        'salary' : 10000,
    }

    data = Employee.objects.all() 
    response = { 'employees': list(data.values('name', 'salary'))}
    

    return JsonResponse(response)