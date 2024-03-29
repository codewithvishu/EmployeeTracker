from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import Employee
from rest_framework import serializers
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Type 1
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
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EmployeeSerializer(employee, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=404)
        employee.delete()
        return HttpResponse(status=204)


# Type 2
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
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return HttpResponse(status=404)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, pk):
        data = JSONParser().parse(request)
        employee = self.get_object(pk)
        if not employee:
            return HttpResponse(status=404)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return HttpResponse(status=404)
        employee.delete()
        return HttpResponse(status=204)


# Type 3
@api_view(http_method_names=["GET", "POST"])
def employee_list2(request):
    if request.method == "GET":
        employies = Employee.objects.all()
        serializer = EmployeeSerializer(employies, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def employee_detail2(request, pk):
    if request.method == "GET":
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == "PUT":
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=204)


# Type 4
from rest_framework.views import APIView


class EmployeeList3(APIView):

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmployeeDetail3(APIView):

    def get_object(self, pk):
        try:
            employee = Employee.objects.get(id=pk)
            return employee
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
