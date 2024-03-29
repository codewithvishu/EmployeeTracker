from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from Employee.models import Employee
import datetime


class EmployeeViewsTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            firstname="Test",
            lastname="User",
            salary=25000,
            mobile=9819679999,
            email="Test.User@gmail.com",
            DOB=datetime.date(2021, 3, 14),
            joining_date=datetime.date(2021, 11, 11),
            termination_date=datetime.date(2022, 11, 11),
            create_ts=datetime.datetime.now(datetime.UTC),
            mod_ts=datetime.datetime.now(datetime.UTC),
            is_active=True,
        )

    def test_employee_list_view_GET(self):
        url = "/api/v1/employees/" 
        # reverse("Employee:employee-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn(self.employee.firstname, response.json()[0]["firstname"])

    def test_employee_list_view_POST(self):
        url = reverse("Employee:employee-list")
        data = {
            "firstname": "Jane",
            "lastname": "User1",
            "salary": 25000,
            "mobile": 9819679999,
            "email": "Jane.User1@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], "Jane")

    def test_employee_list_view_POST_DateError(self):
        url = reverse("Employee:employee-list")
        data = {
            "firstname": "Jane",
            "lastname": "User1",
            "salary": 25000,
            "mobile": 9819679999,
            "email": "Jane.User1@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2023, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json(),{'non_field_errors': ['Joining date should be lesser than termination date']})
    

    def test_employee_list_view_POST_400(self):
        url = reverse("Employee:employee-list")
        data = {
            "firstname": "Jane",
            "lastname": "User1",
            "salary": 21000,
            "mobile": 9819679999,
            "email": "Jane.User1@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        # self.assertEqual(response.json()["firstname"], "Jane")

    def test_employee_detail_view_GET(self):
        url = reverse("Employee:employee-detail", args=[self.employee.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], self.employee.firstname)

    def test_employee_detail_view_PUT(self):
        url = reverse("Employee:employee-detail", args=[self.employee.pk])
        data = {
            "firstname": "Janne",
            "lastname": "Doe",
            "salary": 60000,
            "mobile": 9819679999,
            "email": "Jane.Doe@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], "Janne")

    def test_employee_detail_view_PUT_400(self):
        url = reverse("Employee:employee-detail", args=[self.employee.pk])
        data = {
            "firstname": "Janne",
            "lastname": "Doe",
            "salary": 2000,
            "mobile": 9819679999,
            "email": "Jane.Doe@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()['salary'], ['salary should be in range of 25000 to 100000'])


    def test_employee_detail_view_DELETE(self):
        url = reverse("Employee:employee-detail", args=[self.employee.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())

    def test_healthcheck(self):
        url = "/healthcheck/"  
        response = self.client.get(url)  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{"Status":"Up"})



class Employee1ViewsTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            firstname="Test",
            lastname="User",
            salary=25000,
            mobile=9819679999,
            email="Test.User@gmail.com",
            DOB=datetime.date(2021, 3, 14),
            joining_date=datetime.date(2021, 11, 11),
            termination_date=datetime.date(2022, 11, 11),
            create_ts=datetime.datetime.now(datetime.UTC),
            mod_ts=datetime.datetime.now(datetime.UTC),
            is_active=True,
        )

    def test_employee_list_view_GET(self):
        url = reverse("Employee:employee1-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertIn(self.employee.firstname, response.json()[0]["firstname"])

    def test_employee_list_view_POST(self):
        url = reverse("Employee:employee1-list")
        data = {
            "firstname": "Jane",
            "lastname": "User1",
            "salary": 25000,
            "mobile": 9819679999,
            "email": "Jane.User1@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], "Jane")

    def test_employee_list_view_POST_400(self):
        url = reverse("Employee:employee1-list")
        data = {
            "firstname": "Jane",
            "lastname": "User1",
            "salary": 21000,
            "mobile": 9819679999,
            "email": "Jane.User1@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        # self.assertEqual(response.json()["firstname"], "Jane")

    def test_employee_detail_view_GET(self):
        url = reverse("Employee:employee1-detail", args=[self.employee.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], self.employee.firstname)

    def test_employee_detail_view_PUT(self):
        url = reverse("Employee:employee1-detail", args=[self.employee.pk])
        data = {
            "firstname": "Janne",
            "lastname": "Doe",
            "salary": 60000,
            "mobile": 9819679999,
            "email": "Jane.Doe@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()["firstname"], "Janne")

    def test_employee_detail_view_PUT_400(self):
        url = reverse("Employee:employee1-detail", args=[self.employee.pk])
        data = {
            "firstname": "Janne",
            "lastname": "Doe",
            "salary": 2000,
            "mobile": 9819679999,
            "email": "Jane.Doe@gmail.com",
            "DOB": datetime.date(2021, 3, 14),
            "joining_date": datetime.date(2021, 11, 11),
            "termination_date": datetime.date(2022, 11, 11),
            "create_ts": datetime.datetime.now(datetime.UTC),
            "mod_ts": datetime.datetime.now(datetime.UTC),
            "is_active": True,
        }
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.json()['salary'], ['salary should be in range of 25000 to 100000'])


    def test_employee_detail_view_DELETE(self):
        url = reverse("Employee:employee1-detail", args=[self.employee.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())

    def test_get_object(self):
        from Employee.views import EmployeeDetail
        emp_detail = EmployeeDetail()
        emp = emp_detail.get_object(self.employee.id)
        self.assertEqual(self.employee, emp)

    def test_get_object_error(self):
        from Employee.views import EmployeeDetail
        emp_detail = EmployeeDetail()
        response = emp_detail.get_object(10)
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response, HttpResponse)
