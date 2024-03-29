https://pytest-django.readthedocs.io/en/latest/

python -m pytest Employee\tests.py

python -m pytest Employee/tests.py::EmployeeViewsTestCase::test_employee_list_view_POST

https://coverage.readthedocs.io/en/7.4.4/
pip install coverage

python -m coverage run -m pytest Employee\tests.py
coverage report -m

git init
git remote add origin https://github.com/codewithvishu/EmployeeTracker.git
git add .

python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
pip freeze