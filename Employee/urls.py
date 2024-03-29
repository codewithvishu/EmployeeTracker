from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

# from .views import SnippetViewSet
from rest_framework import renderers


app_name = 'Employee'

urlpatterns = [
    path('employees/', views.employee_list, name="employee-list"),
    path('employees/<int:pk>/', views.employee_detail, name="employee-detail"),

    path('employees1/',csrf_exempt(views.EmployeeList.as_view()),  name="employee1-list"),
    path('employees1/<int:pk>/',csrf_exempt(views.EmployeeDetail.as_view()), name="employee1-detail"),

]


