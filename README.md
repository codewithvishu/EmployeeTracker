https://pytest-django.readthedocs.io/en/latest/

python -m pytest Employee\tests.py

python -m pytest Employee/tests.py::EmployeeViewsTestCase::test_employee_list_view_POST

https://coverage.readthedocs.io/en/7.4.4/
pip install coverage

python -m coverage run -m pytest Employee\tests.py
python -m coverage run -m pytest .
coverage report -m

git init
git remote add origin https://github.com/codewithvishu/EmployeeTracker.git
git status
git add .
git commit -m "Initial Commit"
git push origin master
git diff

python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
pip freeze