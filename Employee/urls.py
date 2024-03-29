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

    path('employees2/', views.employee_list2, name="employee2-list"),
    path('employees2/<int:pk>/', views.employee_detail2, name="employee2-detail"),

    path('employees3/',views.EmployeeList3.as_view(),  name="employee3-list"),
    path('employees3/<int:pk>/',views.EmployeeDetail3.as_view(), name="employee3-detail"),

]


