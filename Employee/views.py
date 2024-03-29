from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import Employee
from rest_framework import serializers
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views import View


# Create your views here.
@csrf_exempt
def employee_list(request):
    if request.method == "GET":
        employies = Employee.objects.all()
        serializer = EmployeeSerializer(employies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, pk):
    if request.method == "GET":
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return HttpResponse(status=204)


class EmployeeList(View):

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class EmployeeDetail(View):

    def get_object(self, pk):
        try:
            employee = Employee.objects.get(id=pk)
            return employee
        except Employee.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, pk):
        data = JSONParser().parse(request)
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return HttpResponse(status=204)
